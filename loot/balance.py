import requests
import json

class Balance(object):

	apiKey = ""
	apiUrl = ""

	# Balance Urls

	__url_balanceOf = "balance/token/"
	__url_itemBalance = "balance/item/"
	__url_itemBalances = "balance/items/"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# Balance

	def balanceOf(self, account):
		url = self.apiUrl + self.__url_balanceOf + account
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def itemBalance(self, itemAddress, account):
		url = self.apiUrl + self.__url_itemBalance	+ itemAddress + "/" + account	
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def itemBalances(self, account):
		url = self.apiUrl + self.__url_itemBalances	+  account
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)
