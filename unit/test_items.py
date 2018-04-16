import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe
from unit_config import UnitConfig

class TestLootSafeItems(unittest.TestCase):

	apiUrl = UnitConfig.apiUrl
	apiKey = UnitConfig.apiKey
	item = UnitConfig.item
	otpkey = UnitConfig.otpkey
	ethAcc = UnitConfig.ethAcc
	
	def test_getItems(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItems()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)

	def test_getItemAddresses(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItemAddresses()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == dict)

	def test_ledger(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.ledger()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)		

	def test_getItem(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItem(self.item)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == dict)		


	def test_getItemByAddress(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItemByAddress(self.item)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == dict)	

	def test_getSpawnItem(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.spawnItem(self.apiKey, self.otpkey, self.item, self.ethAcc)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['address']) == str)

	def test_clearAvailability(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.clearAvailability(self.apiKey, self.otpkey, self.item, self.ethAcc)

		self.assertEqual(result['status'], 200)					

if __name__ == '__main__':
	unittest.main()