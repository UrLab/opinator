import os
import logging

from MQTTSettings import MQTTSettings

#MQTT Settings
MQTT_SERVER = os.environ.get("MQTT_SERVER", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", "1883"))
MQTT_KEEPALIVE = int(os.environ.get("MQTT_KEEPALIVE", "60"))
MQTT_TOPIC = os.environ.get("MQTT_TOPIC", "default")
mqttSettings = MQTTSettings(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE, MQTT_TOPIC)

#HTTP Settings
HTTP_SERVER_URL= os.environ.get("HTTP_SERVER_URL", "http://localhost:8080")
HTTP_SERVER_SECRET = os.environ.get("HTTP_SERVER_SECRET", "secret")

#Log Settings
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(levelname)s:%(name)s:[%(asctime)s] %(message)s"
LOG_DATEFORMAT = "%Y-%m-%d %H:%M:%S"
LOG_PATH = "../logs/mqtt2http.log"

