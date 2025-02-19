#Standard imports
import logging
import os

#Project imports
from MQTTClient	import MQTTClient
from HttpService import HttpService
import settings

print(settings.MQTT_TOPIC)
print(settings.HTTP_SERVER_SECRET)

#Logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(
	filename=f"{os.path.dirname(os.path.abspath(__file__))}/mqtt2http.log", 
	level=settings.LOG_LEVEL, 
	filemode="a", 
	format=settings.LOG_FORMAT, 
	datefmt=settings.LOG_DATEFORMAT
)
logging.info(" ")
logging.info("-"*30)
logging.info(" ")
print("coucou")
#MQTT2HTTP
httpService = HttpService(settings.HTTP_SERVER_URL, settings.HTTP_SERVER_SECRET)
mqttClient = MQTTClient(settings.mqttSettings, httpService)
print("hihi")
mqttClient.start()

