from MQTTClient	import MQTTClient
from HttpService import HttpService
from MQTTSettings import MQTTSettings
import settings

mqttSettings = MQTTSettings(settings.MQTT_SERVER, settings.MQTT_PORT, MQTT_KEEPALIVE)
httpService = HttpService(INCUBATOR_BASE_URL, INCUBATOR_SECRET)

mqttClient.start()
httpService.run(mqttClient.isUp())

