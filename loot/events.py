import requests

class Events(object):

	apiKey = ""
	apiUrl = ""

	# Events Urls

	__url_fetchevents= "/events"

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
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"