#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

#include "esp32_config.h"

// ======================
// Setup
// ======================

void setup() {

  Serial.begin(115200);

  Serial.println();
  Serial.println("=================================");
  Serial.println("ESP32 Motion Sensor Started");
  Serial.println("=================================");

  // ======================
  // PIR sensor
  // ======================

  pinMode(PIR_PIN, INPUT);

  // ======================
  // WiFi connection
  // ======================

  WiFi.begin(WIFI_NAME, WIFI_PASSWORD);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {

    delay(1000);

    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi connected");

  Serial.print("ESP32 IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.println();
}

// ======================
// Main loop
// ======================

void loop() {

  // ======================
  // Read PIR sensor
  // ======================

  int motion = digitalRead(PIR_PIN);

  // ======================
  // Send data if WiFi connected
  // ======================

  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;

    http.begin(SERVER_URL);

    http.addHeader("Content-Type", "application/json");

    // ======================
    // Create JSON payload
    // ======================

    StaticJsonDocument<256> doc;

    doc["motion"] = motion;

    // uptime ESP32 in milliseconds
    doc["timestamp"] = millis();

    String jsonString;

    serializeJson(doc, jsonString);

    // ======================
    // Send POST request
    // ======================

    int httpResponseCode = http.POST(jsonString);

    // ======================
    // Serial monitor logs
    // ======================

    Serial.println("-------------");

    Serial.print("Motion detected: ");
    Serial.println(motion);

    Serial.print("POST Response Code: ");
    Serial.println(httpResponseCode);

    Serial.print("JSON sent: ");
    Serial.println(jsonString);

    Serial.println("-------------");

    http.end();
  }

  else {

    Serial.println("WiFi disconnected");
  }

  // ======================
  // Wait before next request
  // ======================

  delay(SEND_INTERVAL);
}