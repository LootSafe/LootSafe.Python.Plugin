from lootsafe import LootSafe

apiUrl = "http://localhost:1337/v1"
apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"

ethAcc = "0x2e4d853394e3d06d439b68ed7785e36a14f3a154"
item = "0xf98cf41cf795ef4305237cb7485d35f028ade4b2"
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
	print(lootsafe.balance.balanceOf_GET(ethAcc))
	print(lootsafe.balance.itemBalance_GET(item, ethAcc))
	print(lootsafe.balance.itemBalances_GET(ethAcc))

if crafterFlag is True:
	print('\n - Crafter - ')
	print(lootsafe.crafter.getCraftables_GET())
	print(lootsafe.crafter.getDeconstructables_GET())
	print(lootsafe.crafter.getDeconstructionRecipe_GET(item))
	print(lootsafe.crafter.getRecipe_GET(item))
	print(lootsafe.crafter.newRecipe_POST(apiKey, otpkey, '123456', ["1212", "3434"] , [1,2]))
	print(lootsafe.crafter.removeRecipe_POST(apiKey, otpkey, item))

if eventsFlag is True:
	print('\n - Events - ')
	print(lootsafe.events.fetchEvents_GET())

if globalsFlag is True:
	print('\n - Globals - ')
	print(lootsafe.globe.getMeta_GET())
	print(lootsafe.globe.getTokenAddress_GET())
	print(lootsafe.globe.newItem_POST(apiKey, otpkey, "FNX45", "fnx45", 120000, "metadata"))

if itemsFlag is True:
	print('\n - Items - ')
	print(lootsafe.items.getItems_GET())
	print(lootsafe.items.getItemAddresses_GET())
	print(lootsafe.items.ledger_GET())
	print(lootsafe.items.getItem_GET(item))
	print(lootsafe.items.getItemByAddress_GET(item))

if lootboxFlag is True:
	print('\n - LootBox - ')
	print(lootsafe.lootbox.getChances_GET())
	print(lootsafe.lootbox.getCost_GET())
	print(lootsafe.lootbox.getItems_GET(rarity))
	print(lootsafe.lootbox.addItem_POST(apiKey, otpkey, item, rarity))
	print(lootsafe.lootbox.updateChance_GET(apiKey, otpkey, "1", "2", "3"))
	print(lootsafe.lootbox.updateLootBoxCost_GET(apiKey, otpkey, "1"))