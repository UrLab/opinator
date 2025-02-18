from requests import post

class HttpService:
	def __init__(self, url, secret):
		self.url = url
		self.secret = secret
	
	def run(self, isUp):
		requests.post(
		    self.url + '/space/change_status',
		    data={
		        'open': 1 if isUp else 0,
		        'secret': self.secret,
		    }
		)

