import requests

class Crafter(object):

	apiKey = ""
	apiUrl = ""

	# Crafter Urls

	__url_getCraftables = "/craftables"
	__url_getDeconstructables = "/deconstructables"
	__url_getDeconstructablesRecipe = "/recipe/deconstruction/get/"
	__url_getRecipe = "/recipe/get/"
	__url_newRecipe = "/recipe/new"
	__url_removeRecipe = "/recipe/remove"
	__url_newDeconstructionRecipe = "/recipe/deconstruction/new"

	# Init

	def __init__(self, apiUrl, apiKey):
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

	# Crafter

	def	getCraftables(self):		
		url = self.apiUrl + self.__url_getCraftables
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";

	def getDeconstructables(self):
		url = self.apiUrl + self.__url_getDeconstructables
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def getDeconstructionRecipe(self, item):
		url = self.apiUrl + self.__url_getDeconstructablesRecipe + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def getRecipe(self, item):
		url = self.apiUrl + self.__url_getRecipe + item
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def newRecipe(self, apiKey, otp, result, materials, counts):
		url = self.apiUrl + self.__url_newRecipe
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'result': result, 'materials': materials, 'counts': counts}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	def removeRecipe(self, apiKey, otp, item):		
		url = self.apiUrl + self.__url_removeRecipe
		headers = {'key' : apiKey, 'otp' : otp}
		postData = {'item' : item}
		response = requests.post(url, data=postData, headers=headers)
		if response.status_code == 200:
			return response.json()
		else:
			return "{'status': " + str(response.status_code) + ", 'message': '" + response.text + "', 'data' : 'null'}";


	#def newDeconstructionRecipe(self, apiKey, otp):			