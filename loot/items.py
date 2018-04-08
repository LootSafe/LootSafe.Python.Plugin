import requests

class Items(object):

	apiKey = ""
	apiUrl = ""

	# Items Urls

	__url_getItemsItems = "/item/list/"
	__url_getItem = "/item/get/"
	__url_getItemByAddress = "/item/get/address/"
	__url_getItemAddresses = "/item/addresses/get"
	__url_ledger = "/item/ledger"

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
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	
	def getItemAddresses(self):
		url = self.apiUrl + self.__url_getItemAddresses
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def ledger(self):
		url = self.apiUrl + self.__url_ledger
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def getItem(self, item):
		url = self.apiUrl + self.__url_getItem + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def getItemByAddress(self, item):
		url = self.apiUrl + self.__url_getItemByAddress + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";