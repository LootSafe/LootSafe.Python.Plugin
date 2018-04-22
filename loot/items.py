import requests
import json

class Items(object):

	apiKey = ""
	apiUrl = ""

	# Items Urls

	__url_getItemsItems = "item/list/"
	__url_getItem = "item/get/"
	__url_getItemByAddress = "item/get/address/"
	__url_getItemAddresses = "item/addresses/get"
	__url_ledger = "item/ledger"	
	__url_spawnItem = "item/spawn"
	__url_clearAvailability = "item/clearAvailability"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# Items

	def getItems(self):
		url = self.apiUrl + self.__url_getItemsItems
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	
	def getItemAddresses(self):
		url = self.apiUrl + self.__url_getItemAddresses
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)


	def ledger(self):
		url = self.apiUrl + self.__url_ledger
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def getItem(self, itemAddress):
		url = self.apiUrl + self.__url_getItem + itemAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def getItemByAddress(self, itemAddress):
		url = self.apiUrl + self.__url_getItemByAddress + itemAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def clearAvailability(self, apiKey, otp, itemAddress):
		url = self.apiUrl + self.__url_clearAvailability
		headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json' , "dataType" : "json", 'key' : apiKey, 'otp' : otp}
		postData = {'itemAddress' : itemAddress }
		response = requests.post(url, data = json.dumps(postData), headers = headers)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)	

	def spawnItem(self, apiKey, otp, itemAddress, account):
		url = self.apiUrl + self.__url_spawnItem
		headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json' , "dataType" : "json", 'key' : apiKey, 'otp' : otp}
		postData = {'itemAddress' : itemAddress, 'to' : account }
		response = requests.post(url, data = json.dumps(postData), headers = headers)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)	