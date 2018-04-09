import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe

class TestLootSafeCrafter(unittest.TestCase):

	apiUrl = "http://localhost:1337/v1"
	apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"
	ethAcc = "0xcca93ab17df77f41863d76f222054d01c16d868a"
	item = "0xc359fb8fcf206c321fdb90236afbdc71e8c7e845"
	otpkey = "otpkey"

	def test_getCraftables(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getCraftables()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Craftables fetched')
		self.assertTrue(type(result['data']) == list)

	def test_getDeconstructables(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getDeconstructables()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Deconstructables fetched')
		self.assertTrue(type(result['data']) == list)
		self.assertIsNotNone(result['data'])

	def test_getDeconstructionRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getDeconstructionRecipe(self.item)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Recipe fetched')
		self.assertTrue(type(result['data']) == list)
		self.assertIsNotNone(result['data'])

	def test_getRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getRecipe(self.item)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Recipe fetched')
		self.assertTrue(type(result['data']) == list)
		self.assertIsNotNone(result['data'])

	def test_newRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.newRecipe(self.apiKey, self.otpkey, '123456', ["1212", "3434"] , [1,2])		

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'New recipe added')

	def test_removeRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.removeRecipe(self.apiKey, self.otpkey, self.item)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Recipe removed')

if __name__ == '__main__':
	unittest.main()