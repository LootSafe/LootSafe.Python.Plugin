import sys
import unittest
import json
import unit_config

sys.path.append("..")

from lootsafe import LootSafe
from unit_config import UnitConfig

class TestLootSafeBalance(unittest.TestCase):

	apiUrl = UnitConfig.apiUrl
	apiKey = UnitConfig.apiKey
	ethAcc = UnitConfig.ethAcc

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