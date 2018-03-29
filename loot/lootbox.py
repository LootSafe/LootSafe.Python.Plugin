import requests

class LootBox(object):

	apiKey = ""
	apiUrl = ""

	# LootBox Urls

	__url_getChances = "/lootbox/chances"
	__url_getCost = "/lootbox/cost"
	__url_getItemsLootBox = "/lootbox/items/"
	__url_addItem = "/lootbox/item/add"
	__url_updateChance = "/lootbox/chances/update/"
	__url_updateLootBoxCost = "/lootbox/cost/"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# LootBox

	def getChances_GET(self):
		url = self.apiUrl + self.__url_getChances
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	
	def getCost_GET(self):
		url = self.apiUrl + self.__url_getCost
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def getItems_GET(self, rarity):
		url = self.apiUrl + self.__url_getItemsLootBox + rarity
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def addItem_POST(self, apiKey, otp, item, rarity):
		url = self.apiUrl + self.__url_addItem
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'item' : item, 'rarity' : rarity}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	
	def updateChance_GET(self, apiKey, otp, epic, rare, uncommon):	
		url = self.apiUrl + self.__url_updateChance + epic + "/" + rare + "/" + uncommon
		headers = {'key' : apiKey, 'otp' : otp}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def updateLootBoxCost_GET(self, apiKey, otp, cost):
		url = self.apiUrl + self.__url_updateLootBoxCost + cost
		headers = {'key' : apiKey, 'otp' : otp}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";