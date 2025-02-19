import paho.mqtt.client as mqtt
import logging

logger = logging.getLogger(__name__)

class MQTTClient:
	def __init__(self, mqttSettings, service):
		self.service = service
		try:
			self.client = mqtt.Client()
			self.client.on_connect = self.on_connect
			self.client.on_message = self.on_message
			self.client.connect(mqttSettings.mqttServerIp, mqttSettings.mqttServerPort, mqttSettings.mqttKeepAlive)
			self.topic = mqttSettings.mqttTopic
		except Exception as e:
			logger.exception(f"Exception in MQTT listener, could not proceed, stopping. Error : {e}")

	def on_connect(self, client, userdata, flags, rc):
		logger.info("Connected with result code " + str(rc))
		self.client.subscribe(self.topic)

	def on_message(self, client, userdata, msg):
		logger.info(msg.topic + " " + str(msg.payload))
		if msg.topic == self.topic:
			try:
				assert msg.payload in (b"0", b"1")
			except AssertionError:
				logger.warning(f"Invalid message received in topic <{topic}> : <{msg.payload}>")
			else:
				is_up = msg.payload == b"1"
				self.service.run(is_up)

	def start(self):
		self.client.loop_forever()

