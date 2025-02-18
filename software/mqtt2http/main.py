from MQTTClient	import MQTTClient
from HttpService import HttpService
from MQTTSettings import MQTTSettings
import settings

mqttSettings = MQTTSettings(MQTT_SERVER, MQTT_PORT, MQTT_KEEPALIVE)
mqttClient = MQTTClient(mqttSettings)
httpService = HttpService(INCUBATOR_BASE_URL, INCUBATOR_SECRET)

mqttClient.start()
httpService.run(mqttClient.isUp())

