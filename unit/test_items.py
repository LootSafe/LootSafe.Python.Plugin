import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe

class TestLootSafeItems(unittest.TestCase):

	apiUrl = "http://localhost:1337/v1"
	apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"
	item = "0xc359fb8fcf206c321fdb90236afbdc71e8c7e845"

	def test_getItems(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItems()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Items fetched')
		self.assertTrue(type(result['data']) == list)

	def test_getItemAddresses(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItemAddresses()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Item addresses fetched')
		self.assertTrue(type(result['data']) == dict)

	def test_ledger(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.ledger()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Items fetched')
		self.assertTrue(type(result['data']) == list)		

	def test_getItem(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItem(self.item)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Item fetched')
		self.assertTrue(type(result['data']) == dict)		


	def test_getItemByAddress(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.items.getItemByAddress(self.item)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Item fetched')
		self.assertTrue(type(result['data']) == dict)		

if __name__ == '__main__':
	unittest.main()