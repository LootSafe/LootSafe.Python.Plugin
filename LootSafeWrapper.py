import requests

class LootSafe(object):
    
	apiKey = ""
	apiUrl = ""

	# Balance Urls

	__url_balanceOf = "/balance/token/"
	__url_itemBalance = "/balance/item/"
	__url_itemBalances = "/balance/items/"

	# Crafter Urls

	__url_getCraftables = "/craftables"
	__url_getDeconstructables = "/deconstructables"
	__url_getDeconstructablesRecipe = "/recipe/deconstruction/get/"
	__url_getRecipe = "/recipe/get/"
	__url_newRecipe = "/recipe/new"
	__url_removeRecipe = "/recipe/remove"
	__url_newDeconstructionRecipe = "/recipe/deconstruction/new"

	# Events Urls

	__url_fetchevents= "/events"

	# Globals Urls

	__url_newItem = "/item/new"
	__url_spawnItem = "/item/new"
	__url_clearAvailability = "/item/new"
	__url_meta = "/"
	__url_getTokenAddress = "/address/token/"

	# Items Urls

	__url_getItemsItems = "/item/list/"
	__url_getItem = "/item/get/"
	__url_getItemByAddress = "/item/get/address/"
	__url_getItemAddresses = "/item/addresses/get"
	__url_ledger = "/item/ledger"

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

	# Balance

	def balance_balanceOf_GET(self, ethAcc):
		url = self.apiUrl + self.__url_balanceOf + ethAcc
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def balance_itemBalance_GET(self, itemAddr, ethAcc):
		url = self.apiUrl + self.__url_itemBalance	+ itemAddr + "/" + ethAcc	
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def balance_itemBalances_GET(self, ethAcc):
		url = self.apiUrl + self.__url_itemBalances	+  ethAcc
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	# Crafter

	def	crafter_getCraftables_GET(self):		
		url = self.apiUrl + self.__url_getCraftables
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def crafter_getDeconstructables_GET(self):
		url = self.apiUrl + self.__url_getDeconstructables
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def crafter_getDeconstructionRecipe_GET(self, item):
		url = self.apiUrl + self.__url_getDeconstructablesRecipe + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def crafter_getRecipe_GET(self, item):
		url = self.apiUrl + self.__url_getRecipe + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def crafter_newRecipe_POST(self, apiKey, otp, result, materials, counts):
		url = self.apiUrl + self.__url_newRecipe
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'result': result, 'materials': materials, 'counts': counts}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def crafter_removeRecipe_POST(self, apiKey, otp, item):		
		url = self.apiUrl + self.__url_removeRecipe
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'item' : item}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	#def newDeconstructionRecipe_POST(self, apiKey, otp):

	# Events

	def events_fetchEvents_GET(self):
		url = self.apiUrl + self.__url_fetchevents
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	# Globals

	def globals_getMeta_GET(self):		
		url = self.apiUrl + self.__url_meta
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def globals_getTokenAddress_GET(self):		
		url = self.apiUrl + self.__url_getTokenAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def globals_newItem_POST(self, apiKey, otp, name, id, totalSupply, metadata):
		url = self.apiUrl + self.__url_newItem
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'name' : name, 'id' : id, 'totalSupply' : totalSupply, 'metadata' : metadata}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	#spawnItem_POST(string apiKey, string otp)
	#clearAvailability_POST(string apiKey, string otp)

	# Items

	def items_getItems_GET(self):
		url = self.apiUrl + self.__url_getItemsItems
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	
	def items_getItemAddresses_GET(self):
		url = self.apiUrl + self.__url_getItemAddresses
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def items_ledger_GET(self):
		url = self.apiUrl + self.__url_ledger
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def items_getItem_GET(self, item):
		url = self.apiUrl + self.__url_getItem + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def items_getItemByAddress_GET(self, item):
		url = self.apiUrl + self.__url_getItemByAddress + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	# LootBox

	def lootbox_getChances_GET(self):
		url = self.apiUrl + self.__url_getChances
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	
	def lootbox_getCost_GET(self):
		url = self.apiUrl + self.__url_getCost
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def lootbox_getItems_GET(self, rarity):
		url = self.apiUrl + self.__url_getItemsLootBox + rarity
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def lootbox_addItem_POST(self, apiKey, otp, item, rarity):
		url = self.apiUrl + self.__url_addItem
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'item' : item, 'rarity' : rarity}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	
	def lootbox_updateChance_GET(self, apiKey, otp, epic, rare, uncommon):	
		url = self.apiUrl + self.__url_updateChance + epic + "/" + rare + "/" + uncommon
		headers = {'key' : apiKey, 'otp' : otp}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def lootbox_updateLootBoxCost_GET(self, apiKey, otp, cost):
		url = self.apiUrl + self.__url_updateLootBoxCost + cost
		headers = {'key' : apiKey, 'otp' : otp}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";		