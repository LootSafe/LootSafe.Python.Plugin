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

 Endpoint  | Type | Auth | Status |
|---|---|---|---|
| **Balance**   |   |   |   |
| balance_balanceOf_GET(address)  | **GET**  | OPEN  | - [x] Available |
| balance_itemBalances_GET(address)  | **GET**  | OPEN  | - [x] Available |
| balance_itemBalance_GET(itemAddress, address)  | **GET**  | OPEN   | - [x] Available |
| **Crafter**   |   |   |   |
| crafter_getCraftables_GET()  | **GET**  | OPEN   | - [x] Available |
| crafter_getDeconstructables_GET()  | **GET**  | OPEN   | - [x] Available |
| crafter_getDeconstructionRecipe_GET(item)  | **GET**  | OPEN   | - [x] Available |
| crafter_getRecipe_GET(item) | **GET**  | OPEN   | - [x] Available |
| crafter_newRecipe_POST(apiKey, otp, result, materials, counts)  | **POST**  | AUTH   | - [x] Available |
| crafter_removeRecipe_POST(apiKey, otp, item)  | **POST**  | AUTH   | - [x] Available |
| ~~newDeconstructionRecipe_POST(apiKey, otp)~~ | **POST**  | AUTH   | - [ ] Available |
| **Events**  |   |   |   |
| events_fetchEvents_GET()  | **GET**  | OPEN   | - [x] Available |
| **Globals**  |   |   |   |
| globals_getMeta_GET()  | **GET**  | OPEN   | - [x] Available |
| globals_getTokenAddress_GET()  | **GET**  | OPEN   | - [x] Available |
| globals_newItem_POST(apiKey, otp, name, id, totalSupply, metadata) | **POST**  | AUTH   | - [x] Available |
| ~~spawnItem_POST(apiKey, otp)~~  | **POST**   | AUTH   | - [ ] Available |
| ~~clearAvailability_POST(apiKey, otp)~~  | **POST**   | AUTH   | - [ ] Available |
| **Items**  |   |   |   |
| items_getItems_GET()  | **GET**  | OPEN   | - [x] Available |
| items_getItemAddresses_GET()  | **GET**  | OPEN   | - [x] Available |
| items_ledger_GET()  | **GET**  | OPEN   | - [x] Available |
| items_getItem_GET(item)  | **GET**  | OPEN   | - [x] Available |
| items_getItemByAddress_GET(item) | **GET**  | OPEN   | - [x] Available |
| **LootBox** |   |   |   |
| lootbox_getChances_GET()  | **GET**  | OPEN   | - [x] Available |
| lootbox_getCost_GET()  | **GET**  | OPEN   | - [x] Available |
| lootbox_getItems_GET(rarity)  | **GET**  | OPEN   | - [x] Available |
| lootbox_addItem_POST(apikey, opt, item, rarity)  | **POST**  | AUTH  | - [x] Available |
| lootbox_updateChance_GET(apikey, opt, epic,  rare, uncommon) | **GET**  | AUTH  | - [x] Available |
| lootbox_updateLootBoxCost_GET(apikey, opt, cost)  | **GET**  | AUTH  | - [x] Available |

## Issues & Future Development

* **[Server Issue]** crafter.newDeconstructionRecipe_POST
* **[Server Issue]** global.spawnItem_POST
* **[Server Issue]** global.clearAvailability_POST
