import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe

class TestLootSafeBalance(unittest.TestCase):

	apiUrl = "http://localhost:1337/v1"
	apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"
	ethAcc = "0xcca93ab17df77f41863d76f222054d01c16d868a"

	def test_balanceOf(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.balance.balanceOf(self.ethAcc)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Balance fetched')
		self.assertIsNotNone(result['data'])
		self.assertTrue(result['data'].isdigit())

	def test_itemBalance(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.balance.balanceOf(self.ethAcc)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Balance fetched')
		self.assertIsNotNone(result['data'])
		self.assertTrue(result['data'].isdigit())


	def test_itemBalances(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.balance.balanceOf(self.ethAcc)

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Balance fetched')
		self.assertIsNotNone(result['data'])
		self.assertTrue(result['data'].isdigit())

if __name__ == '__main__':
	unittest.main()