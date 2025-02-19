#Standard imports
import logging

#Project imports
from MQTTClient	import MQTTClient
from HttpService import HttpService
import settings

#Logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(
	filename=settings.LOG_PATH, 
	level=settings.LOG_LEVEL, 
	filemode="a", 
	format=settings.LOG_FORMAT, 
	datefmt=settings.LOG_DATEFORMAT
)
logging.info(" ")
logging.info("-"*30)
logging.info(" ")
#MQTT2HTTP
httpService = HttpService(settings.HTTP_SERVER_URL, settings.HTTP_SERVER_SECRET)
mqttClient = MQTTClient(settings.mqttSettings, httpService)
mqttClient.start()

