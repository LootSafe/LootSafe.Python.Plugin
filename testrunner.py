from lootsafe import LootSafe

apiUrl = "http://localhost:1337/v1"
apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"

ethAcc = "0xcca93ab17df77f41863d76f222054d01c16d868a"
item = "0xc359fb8fcf206c321fdb90236afbdc71e8c7e845"
rarity = "uncommon"
otpkey = "otpkey"

lootsafe = LootSafe(apiUrl, apiKey)

balanceFlag = True
crafterFlag = True
eventsFlag = True
globalsFlag = True
itemsFlag = True
lootboxFlag = True

print()
print("=== TestRunner ===")

if balanceFlag is True:
	print('\n - Balance - ')
	print(lootsafe.balance.balanceOf(ethAcc))
	print(lootsafe.balance.itemBalance(item, ethAcc))
	print(lootsafe.balance.itemBalances(ethAcc))

if crafterFlag is True:
	print('\n - Crafter - ')
	print(lootsafe.crafter.getCraftables())
	print(lootsafe.crafter.getDeconstructables())
	print(lootsafe.crafter.getDeconstructionRecipe(item))
	print(lootsafe.crafter.getRecipe(item))
	print(lootsafe.crafter.newRecipe(apiKey, otpkey, '123456', ["1212", "3434"] , [1,2]))
	print(lootsafe.crafter.removeRecipe(apiKey, otpkey, item))

if eventsFlag is True:
	print('\n - Events - ')
	print(lootsafe.events.fetchEvents())

if globalsFlag is True:
	print('\n - Globals - ')
	print(lootsafe.globe.getMeta())
	print(lootsafe.globe.getTokenAddress())
	print(lootsafe.globe.newItem(apiKey, otpkey, "FNX45", "fnx45", 120000, "metadata"))

if itemsFlag is True:
	print('\n - Items - ')
	print(lootsafe.items.getItems())
	print(lootsafe.items.getItemAddresses())
	print(lootsafe.items.ledger())
	print(lootsafe.items.getItem(item))
	print(lootsafe.items.getItemByAddress(item))

if lootboxFlag is True:
	print('\n - LootBox - ')
	print(lootsafe.lootbox.getChances())
	print(lootsafe.lootbox.getCost())
	print(lootsafe.lootbox.getItems(rarity))
	print(lootsafe.lootbox.addItem(apiKey, otpkey, item, rarity))
	print(lootsafe.lootbox.updateChance(apiKey, otpkey, "1", "2", "3"))
	print(lootsafe.lootbox.updateLootBoxCost(apiKey, otpkey, "1"))