from requests import post
import logging

logger = logging.getLogger(__name__)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)

class HttpService:
	def __init__(self, url, secret):
		self.url = url
		self.secret = secret
	
	def run(self, isUp):
		logger.info(f"Sending HTTP Request to {self.url} with state {isUp}")
		requests.post(
		    self.url,
		    data={
		        'open': 1 if isUp else 0,
		        'secret': self.secret,
		    }
		)
		logger.info(f"HTTP Request sent to {self.url} with state {isUp}")

