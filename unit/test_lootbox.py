import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe
from unit_config import UnitConfig

class TestLootSafeBalance(unittest.TestCase):

	apiUrl = UnitConfig.apiUrl
	apiKey = UnitConfig.apiKey	
	otpKey = UnitConfig.otpKey
	itemAddress = UnitConfig.itemAddress
	rarity = UnitConfig.rarity

	def test_getChances(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.getChances()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)

	def test_getCost(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.getCost()

		self.assertEqual(result['status'], 200)
		self.assertTrue(result['data'].isdigit())

	def test_getItems(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.getItems(self.rarity)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)

	def test_addItem(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.addItem(self.apiKey, self.otpKey, self.itemAddress, self.rarity)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == dict)

	def test_updateChance(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.updateChance(self.apiKey, self.otpKey, "1", "2", "3")

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == dict)

	def test_updateLootBoxCost(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.updateLootBoxCost(self.apiKey, self.otpKey, "1")
		
		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == dict)

if __name__ == '__main__':
	unittest.main()