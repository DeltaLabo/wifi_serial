#ifndef WIFISERIAL_H
#define WIFISERIAL_H

#include <WiFi.h>
#include <HTTPClient.h>

// WiFiSerial class for sending data over WiFi using HTTP POST requests
class WiFiSerial {
public:
  // Constructor to initialize WiFi credentials and server URL
  WiFiSerial(const char* ssid, const char* password, const char* serverUrl);

  // Method to connect to WiFi, returns 0 on success, 1 on failure
  int begin();

  // Methods to send data to the server
  int print(const String &message);
  int println(const String &message);
  int write(const uint8_t *buffer, size_t size);

private:
  const char* ssid;
  const char* password;
  const char* serverUrl;

  // Helper method to send data to the server, returns 0 on success, non-zero on failure
  int sendToServer(const String &message);
};

#endif // WIFISERIAL_H
