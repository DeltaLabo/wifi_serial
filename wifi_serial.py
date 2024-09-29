from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import threading
import time

# Class to handle the data buffer with thread safety
class DataBuffer:
    def __init__(self):
        self.buffer = ""
        self.lock = threading.Lock()

    def append(self, data):
        # Append data to the buffer in a thread-safe manner
        with self.lock:
            self.buffer += data

    def read(self, size):
        # Read a specified number of bytes from the buffer in a thread-safe manner
        with self.lock:
            data = self.buffer[:size]
            self.buffer = self.buffer[size:]
        return data

    def read_until(self, delimiter):
        # Read from the buffer until the specified delimiter is found
        with self.lock:
            if delimiter in self.buffer:
                before, after = self.buffer.split(delimiter, 1)
                self.buffer = after
                return before + delimiter
            return None

    def readline(self):
        # Read a line from the buffer (up to and including '\n')
        return self.read_until('\n')

# HTTP request handler class
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global data_buffer
        # Get the length of the incoming data
        content_length = int(self.headers['Content-Length'])
        # Read the incoming data
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Append the data to the buffer
        data_buffer.append(post_data)
        
        # Send a 200 OK response
        self.send_response(200)
        self.end_headers()

# Thread class to run the server
class ServerThread(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.daemon = True
        self.server_address = ('', port)
        self.httpd = HTTPServer(self.server_address, RequestHandler)
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        print(f'Starting server on {local_ip}:{port}...')

    def run(self):
        # Start the server
        self.httpd.serve_forever()

# Main class for WiFi serial
class WiFiSerial:
    def __init__(self, port, timeout=None):
        global data_buffer
        data_buffer = DataBuffer()
        self.timeout = timeout
        # Start the server thread
        self.server_thread = ServerThread(port)
        self.server_thread.start()

    def read(self, size=1):
        # Read a specified number of bytes with an optional timeout
        end_time = None if self.timeout is None else (time.time() + self.timeout)
        
        while True:
            data = data_buffer.read(size)
            if data:
                return data
        
            if self.timeout is not None and time.time() > end_time:
                raise TimeoutError("Read operation timed out")
        
            time.sleep(0.01)  # Avoid busy waiting

    def readline(self):
        # Read a line with an optional timeout
        end_time = None if self.timeout is None else (time.time() + self.timeout)
        
        while True:
            line = data_buffer.readline()
            if line:
                return line
        
            if self.timeout is not None and time.time() > end_time:
                raise TimeoutError("Readline operation timed out")
        
            time.sleep(0.01)  # Avoid busy waiting

    def read_until(self, expected=b'\n'):
        # Read until a specified delimiter is found, with an optional timeout
        end_time = None if self.timeout is None else (time.time() + self.timeout)
        expected_str = expected.decode('utf-8')
        
        while True:
            data = data_buffer.read_until(expected_str)
            if data:
                return data
        
            if self.timeout is not None and time.time() > end_time:
                raise TimeoutError("Read_until operation timed out")
        
            time.sleep(0.01)  # Avoid busy waiting

if __name__ == "__main__":
    import sys

    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    # Create an instance of WiFiSerial
    logger = WiFiSerial(port)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
