from LootSafeWrapper import LootSafe

apiUrl = "http://localhost:1337/v1"
apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"

ethAcc = "0x9ad7858ae4ad66cd22c1d3064ee3749e0cd7a3cc"
item = "0x17db9af544380a0cc6954355c9418cf8f2ee1471"
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
	print(lootsafe.balance_balanceOf_GET(ethAcc))
	print(lootsafe.balance_itemBalance_GET(item, ethAcc))
	print(lootsafe.balance_itemBalances_GET(ethAcc))

if crafterFlag is True:
	print('\n - Crafter - ')
	print(lootsafe.crafter_getCraftables_GET())
	print(lootsafe.crafter_getDeconstructables_GET())
	print(lootsafe.crafter_getDeconstructionRecipe_GET(item))
	print(lootsafe.crafter_getRecipe_GET(item))
	print(lootsafe.crafter_newRecipe_POST(apiKey, otpkey, '123456', ["1212", "3434"] , [1,2]))
	print(lootsafe.crafter_removeRecipe_POST(apiKey, otpkey, item))

if eventsFlag is True:
	print('\n - Events - ')
	print(lootsafe.events_fetchEvents_GET())

if globalsFlag is True:
	print('\n - Globals - ')
	print(lootsafe.globals_getMeta_GET())
	print(lootsafe.globals_getTokenAddress_GET())
	print(lootsafe.globals_newItem_POST(apiKey, otpkey, "FNX45", "fnx45", 120000, "metadata"))

if itemsFlag is True:
	print('\n - Items - ')
	print(lootsafe.items_getItems_GET())
	print(lootsafe.items_getItemAddresses_GET())
	print(lootsafe.items_ledger_GET())
	print(lootsafe.items_getItem_GET(item))
	print(lootsafe.items_getItemByAddress_GET(item))

if lootboxFlag is True:
	print('\n - LootBox - ')
	print(lootsafe.lootbox_getChances_GET())
	print(lootsafe.lootbox_getCost_GET())
	print(lootsafe.lootbox_getItems_GET(rarity))
	print(lootsafe.lootbox_addItem_POST(apiKey, otpkey, item, rarity))
	print(lootsafe.lootbox_updateChance_GET(apiKey, otpkey, "1", "2", "3"))
	print(lootsafe.lootbox_updateLootBoxCost_GET(apiKey, otpkey, "1"))