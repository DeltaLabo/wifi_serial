#include "WiFiSerial.h"

// Constructor to initialize WiFi credentials and server URL
WiFiSerial::WiFiSerial(const char* ssid, const char* password, const char* serverUrl)
  : ssid(ssid), password(password), serverUrl(serverUrl) {}

// Method to connect to WiFi, returns 0 on success, 1 on failure
int WiFiSerial::begin() {
  WiFi.begin(ssid, password);
  unsigned long startAttemptTime = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - startAttemptTime < 10000) {
    delay(500);
  }
  return WiFi.status() == WL_CONNECTED ? 0 : 1; // 0: Success, 1: Failed to connect
}

// Method to send a message to the server, returns 0 on success, non-zero on failure
int WiFiSerial::print(const String &message) {
  return sendToServer(message);
}

// Method to send a message with a newline to the server, returns 0 on success, non-zero on failure
int WiFiSerial::println(const String &message) {
  return sendToServer(message + "\n");
}

// Method to send raw bytes to the server, returns 0 on success, non-zero on failure
int WiFiSerial::write(const uint8_t *buffer, size_t size) {
  String message;
  for (size_t i = 0; i < size; i++) {
    message += (char)buffer[i];
  }
  return sendToServer(message);
}

// Helper method to send data to the server, returns 0 on success, non-zero on failure
int WiFiSerial::sendToServer(const String &message) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "text/plain");
    int httpResponseCode = http.POST(message);
    http.end();
    return httpResponseCode > 0 ? 0 : 2; // 0: Success, 2: HTTP POST failed
  } else {
    return 3; // 3: WiFi not connected
  }
}
