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
| balance.balanceOf_GET(address)  | **GET**  | OPEN  | Available |
| balance.itemBalances_GET(address)  | **GET**  | OPEN  | Available |
| balance.itemBalance_GET(itemAddress, address)  | **GET**  | OPEN   | Available |
| **Crafter**   |   |   |   |
| crafter.getCraftables_GET()  | **GET**  | OPEN   | Available |
| crafter.getDeconstructables_GET()  | **GET**  | OPEN   | Available |
| crafter.getDeconstructionRecipe_GET(item)  | **GET**  | OPEN   | Available |
| crafter.getRecipe_GET(item) | **GET**  | OPEN   | Available |
| crafter.newRecipe_POST(apiKey, otp, result, materials, counts)  | **POST**  | AUTH   | Available |
| crafter.removeRecipe_POST(apiKey, otp, item)  | **POST**  | AUTH   | Available |
| ~~newDeconstructionRecipe_POST(apiKey, otp)~~ | **POST**  | AUTH   | Unavailable |
| **Events**  |   |   |   |
| events.fetchEvents_GET()  | **GET**  | OPEN   | Available |
| **Globals**  |   |   |   |
| globe.getMeta_GET()  | **GET**  | OPEN   | Available |
| globe.getTokenAddress_GET()  | **GET**  | OPEN   | Available |
| globe.newItem_POST(apiKey, otp, name, id, totalSupply, metadata) | **POST**  | AUTH   | Available |
| ~~spawnItem_POST(apiKey, otp)~~  | **POST**   | AUTH   | Unavailable |
| ~~clearAvailability_POST(apiKey, otp)~~  | **POST**   | AUTH   | Unavailable |
| **Items**  |   |   |   |
| items.getItems_GET()  | **GET**  | OPEN   | Available |
| items.getItemAddresses_GET()  | **GET**  | OPEN   | Available |
| items.ledger_GET()  | **GET**  | OPEN   | Available |
| items.getItem_GET(item)  | **GET**  | OPEN   | Available |
| items.getItemByAddress_GET(item) | **GET**  | OPEN   | Available |
| **LootBox** |   |   |   |
| lootbox.getChances_GET()  | **GET**  | OPEN   | Available |
| lootbox.getCost_GET()  | **GET**  | OPEN   | Available |
| lootbox.getItems_GET(rarity)  | **GET**  | OPEN   | Available |
| lootbox.addItem_POST(apikey, opt, item, rarity)  | **POST**  | AUTH  | Available |
| lootbox.updateChance_GET(apikey, opt, epic,  rare, uncommon) | **GET**  | AUTH  | Available |
| lootbox.updateLootBoxCost_GET(apikey, opt, cost)  | **GET**  | AUTH  | Available |

## Issues & Future Development

* **[Server Issue]** crafter.newDeconstructionRecipe_POST
* **[Server Issue]** global.spawnItem_POST
* **[Server Issue]** global.clearAvailability_POST
