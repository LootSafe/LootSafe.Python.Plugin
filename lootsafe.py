from loot.balance import Balance
from loot.crafter import Crafter
from loot.events import Events
from loot.globes import Globals
from loot.items import Items
from loot.lootbox import LootBox

class LootSafe(object):
    
	apiKey = ""
	apiUrl = ""

	balance = None
	crafter = None
	events = None
	globe = None
	items = None
	lootbox = None

	# Init

	def __init__(self, apiUrl, apiKey):
		
		self.apiKey = apiKey	
		self.apiUrl = apiUrl

		self.balance = Balance(apiUrl, apiKey)
		self.crafter = Crafter(apiUrl, apiKey)
		self.events = Events(apiUrl, apiKey)
		self.globe = Globals(apiUrl, apiKey)
		self.items = Items(apiUrl, apiKey)
		self.lootbox = LootBox(apiUrl, apiKey)