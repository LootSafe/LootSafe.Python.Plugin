import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe

class TestLootSafeEvents(unittest.TestCase):

	apiUrl = "http://localhost:1337/v1"
	apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"

	def test_fetchEvents(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.events.fetchEvents()

		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'Events Fetched')
		self.assertTrue(type(result['data']) == list)

if __name__ == '__main__':
	unittest.main()