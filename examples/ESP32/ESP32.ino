#include <Arduino.h>
#include "WiFiSerial.h"

// Replace with your actual WiFi credentials and server URL
const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";
const char* serverUrl = "http://your_pc_ip:your_port/log";

// Create an instance of WiFiSerial
WiFiSerial wifiSerial(ssid, password, serverUrl);

void setup() {
  // Initialize WiFi and handle errors
  int result = wifiSerial.begin();
  if (result != 0) {
    // Handle error (e.g., blink an LED or save the error code)
  }
}

void loop() {
  // Send a message and handle errors
  int result = wifiSerial.println("Hello from ESP32!");
  if (result != 0) {
    // Handle error (e.g., blink an LED or save the error code)
  }
  delay(2000); // Wait for 2 seconds before sending the next message
}
