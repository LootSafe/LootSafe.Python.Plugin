import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe

class TestLootSafeBalance(unittest.TestCase):

	apiUrl = "http://localhost:1337/v1"
	apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"
	item = "0xc359fb8fcf206c321fdb90236afbdc71e8c7e845"
	otpkey = "otpkey"
	rarity = "uncommon"

	def test_getChances(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.getChances()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Chances fetched')
		self.assertTrue(type(result['data']) == list)

	def test_getCost(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.getCost()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'LootBox cost fetched')
		self.assertTrue(result['data'].isdigit())

	def test_getItems(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.getItems(self.rarity)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Items fetched')
		self.assertTrue(type(result['data']) == list)

	def test_addItem(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.addItem(self.apiKey, self.otpkey, self.item, self.rarity)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'New item added to loot table.')
		self.assertTrue(type(result['data']) == dict)

	def test_updateChance(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.updateChance(self.apiKey, self.otpkey, "1", "2", "3")

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Updated lootbox chances')
		self.assertTrue(type(result['data']) == dict)

	def test_updateLootBoxCost(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.lootbox.updateLootBoxCost(self.apiKey, self.otpkey, "1")
		
		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Updated lootbox cost')
		self.assertTrue(type(result['data']) == dict)

if __name__ == '__main__':
	unittest.main()