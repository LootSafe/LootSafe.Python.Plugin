import requests
import json

class Globals(object):

	apiKey = ""
	apiUrl = ""

	# Globals Urls

	__url_meta = ""
	__url_newItem = "item/new"
	__url_getTokenAddress = "address/token/"

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
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def getTokenAddress(self):		
		url = self.apiUrl + self.__url_getTokenAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def newItem(self, apiKey, otp, name, id, totalSupply, metadata):
		url = self.apiUrl + self.__url_newItem
		headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json' , 'key' : apiKey, 'otp' : otp}
		postData = {'name' : name, 'id' : id, 'totalSupply' : totalSupply, 'metadata' : metadata}
		response = requests.post(url, data = json.dumps(postData), headers = headers)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)					