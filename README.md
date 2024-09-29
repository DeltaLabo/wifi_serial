wifi_serial
============
## DeltaLAB - Instituto Tecnológico de Costa Rica

### What is this repository for?

This repository was created to enable WiFi-based, serial-like communication from ESP32 microcontrollers to PCs, for simple wireless logging and debugging purposes.
On the client side (ESP32), it supports the `print`. `println`, and `write` methods of a wired `Serial` interface.
On the server side (Python on a PC), it supports the `read`, `readline`, and `read_until` methods found in the [`pyserial`](https://github.com/pyserial/pyserial) library.

### How do I set up?

* Install Git
* Install Python
* Install Arduino IDE
* Follow these [instructions](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html) to set up the ESP32 in the Arduino IDE
* Clone this repo and run `wifi_serial.py` on your server PC.
* `#include "WiFiSerial.h"` in your main Arduino code file.
* Copy your server address and port (shown by the Python script) to your main Arduino code file.

### Contribution guidelines ###

* If you want to propose a change or need to modify the code for any reason first clone this [repository](https://github.com/DeltaLabo/rsim) to your PC and create a new branch for your changes. Once your changes are complete and fully tested ask the administrator permission to push this new branch into the source.
* If you just want to do local changes instead you can download a zip version of the repository and do all changes locally in your PC. 

### Who do I talk to?

* [Juan J. Rojas](mailto:juan.rojas@itcr.ac.cr)
* [Anthony Arguedas](mailto:antarguedas@estudiantec.r)
