import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe

class TestLootSafeGlobes(unittest.TestCase):

	apiUrl = "http://localhost:1337/v1"
	apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"
	otpkey = "otpkey"

	def test_fetchEvents(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.globe.getMeta()

		self.assertEqual(result['connected'], True)

	def test_getTokenAddress(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.globe.getTokenAddress()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['address']) == str)

	def test_newItem(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.globe.newItem(self.apiKey, self.otpkey, "FNX45", "fnx45", 120000, "metadata")

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Created new item')

if __name__ == '__main__':
	unittest.main()