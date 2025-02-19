import os
import logging

#MQTT Settings
MQTT_SERVER = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.environ.get("MQTT_KEEPALIVE", "60"))
MQTT_TOPIC = os.environ.get("MQTT_TOPIC", "opinator")
mqttSettings = MQTTSettings(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE, MQTT_TOPIC)

#HTTP Settings
INCUBATOR_BASE_URL = "https://urlab.be"
INCUBATOR_SECRET = os.environ.get("INCUBATOR_SECRET", "vairie secrette")

#Log Settings
LOG_LEVEL = logging.DEBUG

