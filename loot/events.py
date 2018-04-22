import requests
import json

class Events(object):

	apiKey = ""
	apiUrl = ""

	# Events Urls

	__url_fetchevents= "events"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# Events

	def fetchEvents(self):
		url = self.apiUrl + self.__url_fetchevents
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)