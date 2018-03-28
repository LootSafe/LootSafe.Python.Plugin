# LootSafe.Python.Plugin
Python implementation of endpoint wrapping the LootSafe API services.

### Environment

Currently working on Python 3.6.4 running on Windows 10.

### Usage

```
python Example.py
```

```
# Import the library

from LootSafeWrapper import LootSafe

# Required Configurable Variables

apiUrl = "http://localhost:1337/v1"
apiKey = "pWpzWuxoKUKAmlHc0wPi7lFS38FTth"

# Creating and Initialzing the LootSafe Object

lootsafe = LootSafe(apiUrl, apiKey)

# Example of basic usage

print()
print("=== Example ===\n")
print(lootsafe.crafter_getCraftables_GET())
```

Output
```
=== Example ===

{'status': 200, 'message': 'Craftables fetched', 'data': []}
```

## Endpoints

### Balance

**Open**

* balance_balanceOf_GET(address)
* balance_itemBalances_GET(address)
* balance_itemBalance_GET(itemAddress, address)

### Crafter

**Open**

* crafter_getCraftables_GET()
* crafter_getDeconstructables_GET()
* crafter_getDeconstructionRecipe_GET(item)
* crafter_getRecipe_GET(item)

**Authenticated**

* crafter_newRecipe_POST(apiKey, otp, result, materials, counts)
* crafter_removeRecipe_POST(apiKey, otp, item)
* **~~newDeconstructionRecipe_POST(apiKey, otp)~~**

### Events

**Open**

* events_fetchEvents_GET()

### Globals

**Open**

* globals_getMeta_GET()
* globals_getTokenAddress_GET()

**Authenticated**

* globals_newItem_POST(apiKey, otp, name, id, totalSupply, metadata)
* **~~spawnItem_POST(apiKey, otp)~~**
* **~~clearAvailability_POST(apiKey, otp)~~**

### Items

**Open**

* items_getItems_GET()
* items_getItemAddresses_GET()
* items_ledger_GET()
* items_getItem_GET(item)
* items_getItemByAddress_GET(item)

### LootBox

**Open**

* lootbox_getChances_GET()
* lootbox_getCost_GET()
* lootbox_getItems_GET(rarity)

**Authenticated**

* lootbox_addItem_POST(apikey, opt, item, rarity)
* lootbox_updateChance_GET(apikey, opt, epic,  rare, uncommon)
* lootbox_updateLootBoxCost_GET(apikey, opt, cost)

## Issues & Future Development

* **[Server Issue]** crafter.newDeconstructionRecipe_POST
* **[Server Issue]** global.spawnItem_POST
* **[Server Issue]** global.clearAvailability_POST
