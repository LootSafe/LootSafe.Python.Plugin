import requests
import json

class Crafter(object):

	apiKey = ""
	apiUrl = ""

	# Crafter Urls

	__url_getCraftables = "craftables"
	__url_getDeconstructables = "deconstructables"
	__url_getDeconstructablesRecipe = "recipe/deconstruction/get/"
	__url_getRecipe = "recipe/get/"
	__url_newRecipe = "recipe/new"
	__url_removeRecipe = "recipe/remove"
	__url_newDeconstructionRecipe = "recipe/deconstruction/new"

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
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def getDeconstructables(self):
		url = self.apiUrl + self.__url_getDeconstructables
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def getDeconstructionRecipe(self, itemAddress):
		url = self.apiUrl + self.__url_getDeconstructablesRecipe + itemAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def getRecipe(self, itemAddress):
		url = self.apiUrl + self.__url_getRecipe + itemAddress
		response = requests.get(url)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def newRecipe(self, apiKey, otp, result, materials, counts):
		url = self.apiUrl + self.__url_newRecipe
		headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json' , 'key' : apiKey, 'otp' : otp}
		postData = {'result': result, 'materials': materials, 'counts': counts}
		response = requests.post(url, data = json.dumps(postData), headers = headers)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def newDestructionRecipe(self, apiKey, otp, result, materials, counts):
		url = self.apiUrl + self.__url_newDeconstructionRecipe
		headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json' , 'key' : apiKey, 'otp' : otp}
		postData = {'result': result, 'materials': materials, 'counts': counts}
		response = requests.post(url, data = json.dumps(postData), headers = headers)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)

	def removeRecipe(self, apiKey, otp, itemAddress):		
		url = self.apiUrl + self.__url_removeRecipe
		headers = {'Content-Type' : 'application/json', 'Accept' : 'application/json' , 'key' : apiKey, 'otp' : otp}
		postData = {'item' : itemAddress}
		response = requests.post(url, data = json.dumps(postData), headers = headers)
		if response.status_code == 200:
			return response.json()
		else:
			result = '{{"status": {0} , "message": {1}, "data" : "null"}}'.format(response.status_code, response.text)			
			return json.loads(result)
