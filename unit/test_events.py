import sys
import unittest
import json

sys.path.append("..")

from lootsafe import LootSafe
from unit_config import UnitConfig

class TestLootSafeEvents(unittest.TestCase):

	apiUrl = UnitConfig.apiUrl
	apiKey = UnitConfig.apiKey
	
	def test_fetchEvents(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.events.fetchEvents()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)

if __name__ == '__main__':
	unittest.main()