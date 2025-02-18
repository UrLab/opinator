import paho.mqtt.client as mqtt
import requests
import logging
import os


logger = logging.getLogger(__name__)

class MQTTSettings:
	def __init__(self,MQTT_SERVER,MQTT_PORT,MQTT_KEEPALIVE,TOPIC):
		self.MQTT_SERVER = MQTT_SERVER
		self.MQTT_PORT = MQTT_PORT
		self.MQTT_KEEPALIVE = MQTT_KEEPALIVE
		self.TOPIC = TOPIC
		pass

class MQTTCLient:
	def __init__(self, settings:MQTTSettings):
		try:
			self.client = mqtt.Client()
			self.client.on_connect = self.on_connect
			self.client.on_message = self.on_message

			self.client.connect(settings.MQTT_SERVER, settings.MQTT_PORT, settings.MQTT_KEEPALIVE)
			self.settings = settings
		except Exception as e:
			logger.exception(f"Exception in MQTT listener, could not proceed, stopping. Error : {e}")


	# The callback for when the client receives a CONNACK response from the server.
	def on_connect(self, client, userdata, flags, rc):
		logger.info("Connected with result code " + str(rc))

		# Subscribing in on_connect() means that if we lose the connection and
		# reconnect then subscriptions will be renewed.
		self.client.subscribe(self.settings.TOPIC)

	# The callback for when a PUBLISH message is received from the server.
	def on_message(self, client, userdata, msg):
		logger.info(msg.topic + " " + str(msg.payload))

		topic = self.settings.TOPIC

		if msg.topic == topic:
			try:
				assert msg.payload in (b"0", b"1")
			except AssertionError:
				logger.warning(f"Invalid message received in topic <{topic}> : <{msg.payload}>")
			else:
				is_up = msg.payload == b"1"
				raise NotImplementedError("Not implemented yet")
