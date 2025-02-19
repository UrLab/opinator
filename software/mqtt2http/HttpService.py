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
		state = 1 if isUp else 0
		logger.info(f"Sending HTTP Request to {self.url} with state {state}")
		response = post(
		    self.url,
		    data={
				'secret': self.secret,
				'open': state
		    }
		)
		print(response.status_code, response.reason)
		logger.info(f"HTTP Request sent to {self.url} with state {state}")

