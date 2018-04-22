import sys
import unittest

sys.path.append("..")

from lootsafe import LootSafe
from unit_config import UnitConfig

class TestLootSafeCrafter(unittest.TestCase):

	apiUrl = UnitConfig.apiUrl
	apiKey = UnitConfig.apiKey
	otpKey = UnitConfig.otpKey
	itemAddress = UnitConfig.itemAddress

	def test_getCraftables(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getCraftables()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)

	def test_getDeconstructables(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getDeconstructables()

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)
		self.assertIsNotNone(result['data'])

	def test_getDeconstructionRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getDeconstructionRecipe(self.itemAddress)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)
		self.assertIsNotNone(result['data'])

	def test_getRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.getRecipe(self.itemAddress)

		self.assertEqual(result['status'], 200)
		self.assertTrue(type(result['data']) == list)
		self.assertIsNotNone(result['data'])

	def test_newRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.newRecipe(self.apiKey, self.otpKey, '123456', ["1212", "3434"] , [1,2])		

		self.assertEqual(result['status'], 200)

	def test_newDestructionRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.newDestructionRecipe(self.apiKey, self.otpKey, '123456', ["1212", "3434"] , [1,2])		

		self.assertEqual(result['status'], 200)

	def test_removeRecipe(self):
		lootsafe = LootSafe(self.apiUrl, self.apiKey)
		result = lootsafe.crafter.removeRecipe(self.apiKey, self.otpKey, self.itemAddress)

		self.assertEqual(result['status'], 200)

if __name__ == '__main__':
	unittest.main()