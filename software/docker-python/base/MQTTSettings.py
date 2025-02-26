import logging

logger = logging.getLogger(__name__)

class MQTTSettings:
	def __init__(self, mqttServerIp, mqttServerPort, mqttKeepAlive, mqttTopic):
		self.mqttServerIp = mqttServerIp
		self.mqttServerPort = mqttServerPort
		self.mqttKeepAlive = mqttKeepAlive
		self.mqttTopic = mqttTopic

