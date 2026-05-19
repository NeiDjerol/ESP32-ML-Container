#ifndef ESP32_CONFIG_H
#define ESP32_CONFIG_H

// ======================
// WiFi settings
// ======================

const char* WIFI_NAME = "YOUR_WIFI_NAME";

const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

// ======================
// FastAPI server
// ======================

const char* SERVER_URL = "http://192.168.0.15:8000/sensor";

// ======================
// PIR sensor pin
// ======================

const int PIR_PIN = 13;

// ======================
// Delay between requests
// ======================

const int SEND_INTERVAL = 5000;

#endif