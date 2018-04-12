import requests

class Balance(object):

	apiKey = ""
	apiUrl = ""

	# Balance Urls

	__url_balanceOf = "/balance/token/"
	__url_itemBalance = "/balance/item/"
	__url_itemBalances = "/balance/items/"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# Balance

	def balanceOf(self, ethAcc):
		url = self.apiUrl + self.__url_balanceOf + ethAcc
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"

	def itemBalance(self, itemAddr, ethAcc):
		url = self.apiUrl + self.__url_itemBalance	+ itemAddr + "/" + ethAcc	
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"

	def itemBalances(self, ethAcc):
		url = self.apiUrl + self.__url_itemBalances	+  ethAcc
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}"