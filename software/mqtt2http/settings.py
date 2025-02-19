import os
import logging

#MQTT Settings
MQTT_SERVER = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.environ.get("MQTT_KEEPALIVE", "60"))
MQTT_TOPIC = os.environ.get("MQTT_TOPIC", "opinator")
mqttSettings = MQTTSettings(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE, MQTT_TOPIC)

#HTTP Settings
HTTP_SERVER_URL= os.environ.get("HTTP_SERVER_URL", "http://localhost:5000")
HTTP_SERVER_SECRET = os.environ.get("HTTP_SERVER_SECRET", "monke need secret")

#Log Settings
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(levelname)s:%(name)s:[%(asctime)s] %(message)s"
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"

