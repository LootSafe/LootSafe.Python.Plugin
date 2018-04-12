import requests

class Globals(object):

	apiKey = ""
	apiUrl = ""

	# Globals Urls

	__url_newItem = "/item/new"
	__url_spawnItem = "/item/new"
	__url_clearAvailability = "/item/new"
	__url_meta = "/"
	__url_getTokenAddress = "/address/token/"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# Globals

	def getMeta(self):		
		url = self.apiUrl + self.__url_meta
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"

	def getTokenAddress(self):		
		url = self.apiUrl + self.__url_getTokenAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"


	def newItem(self, apiKey, otp, name, id, totalSupply, metadata):
		url = self.apiUrl + self.__url_newItem
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'name' : name, 'id' : id, 'totalSupply' : totalSupply, 'metadata' : metadata}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"