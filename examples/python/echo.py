import wifi_serial

# Create an instance of WiFiSerial with the desired port and timeout
serial = wifi_serial.WiFiSerial(port=8080, timeout=5)

try:
    while True:
        try:
            # Reading 10 bytes
            data = serial.read(10)
            print(f"Read data: {data}")

            # Reading a line
            line = serial.readline()
            print(f"Read line: {line}")

            # Reading until 0x17 is found
            data_until = serial.read_until(expected=b'\x17')
            print(f"Read until: {data_until}")
        except TimeoutError as e:
            print(e)
except KeyboardInterrupt:
    print("\nServer stopped by user")
