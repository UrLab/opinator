from MQTTClient	import MQTTClient
from HttpService import HttpService
from MQTTSettings import MQTTSettings
import settings

httpService = HttpService(settings.INCUBATOR_BASE_URL, settings.INCUBATOR_SECRET)
mqttClient = MQTTClient(settings.mqttSettings, httpService)

