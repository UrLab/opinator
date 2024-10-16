#include <Arduino.h>
#include <ESP8266WiFi.h>
#include "PubSubClient.h"
#include "wifi.h"

const char* hostname = "opinator";
const char* ssid = WIFI_H_SSID;
const char* password = WIFI_H_PASSWORD;
const char* mqtt_server = WIFI_H_MQTT_SERVER;

// #define LED D0
#define BOUTON D1
#define LED D0

WiFiClient espClient;
PubSubClient mqttClient(espClient);

int state;
int last_state;


void setup_wifi() {
	delay(10);

	WiFi.mode(WIFI_STA);
	WiFi.hostname(hostname);
	WiFi.setAutoConnect(true);
	WiFi.setAutoReconnect(true);

	WiFi.begin(ssid, password);
	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print("wifi ");
		Serial.println(WiFi.status());
	}
}

void reconnect() {
	String message = String(hostname) + " " + WiFi.localIP().toString() + " " + WiFi.macAddress();
	while (!mqttClient.connected()) {
		if (mqttClient.connect(hostname)) {
			mqttClient.publish("connect", message.c_str());
		} else {
			delay(5000);
		}
	}
}

void setup() {
	Serial.begin(115200);
	Serial.println("Booting");
	pinMode(BOUTON, INPUT_PULLUP);
	pinMode(LED, OUTPUT);
	
	setup_wifi();
	mqttClient.setServer(mqtt_server, 1883);
	Serial.println("Setup done");
}

void open() {
	Serial.println("reading button state");
	state = digitalRead(BOUTON);
	Serial.println(state);
	Serial.println(last_state);
	if (last_state!=state){
		if (state == HIGH){
			Serial.println("open");
			mqttClient.publish(hostname, "1", true);
			digitalWrite(LED, HIGH);
		}
		else{
			Serial.println("close");
			mqttClient.publish(hostname, "0", true);
			digitalWrite(LED, LOW);
		}
	}
	last_state = state;
	delay(500);
}


void loop() {
	Serial.println("loop");
	if (!mqttClient.connected()) {
		Serial.println("reconnecting to mqtt");
		reconnect();
	}
	mqttClient.loop();
	open();
}
