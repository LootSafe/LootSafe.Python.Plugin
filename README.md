# LootSafe.Python.Plugin
Python implementation of endpoint wrapping the LootSafe API services.

### Environment

Currently working on Python 3.6.4 running on Windows 10.

### Usage

```
python example.py
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
print(lootsafe.crafter_getCraftables())
```

Output
```
=== Example ===

{'status': 200, 'message': 'Craftables fetched', 'data': []}
```

### Endpoints

 Endpoint  | Type | Auth | Status |
|---|---|---|---|
| **Balance**   |   |   |   |
| balance.balanceOf(address)  | **GET**  | OPEN  | Available |
| balance.itemBalances(address)  | **GET**  | OPEN  | Available |
| balance.itemBalance(itemAddress, address)  | **GET**  | OPEN   | Available |
| **Crafter**   |   |   |   |
| crafter.getCraftables()  | **GET**  | OPEN   | Available |
| crafter.getDeconstructables()  | **GET**  | OPEN   | Available |
| crafter.getDeconstructionRecipe(item)  | **GET**  | OPEN   | Available |
| crafter.getRecipe(item) | **GET**  | OPEN   | Available |
| crafter.newRecipe(apiKey, otp, result, materials, counts)  | **POST**  | AUTH   | Available |
| crafter.removeRecipe(apiKey, otp, item)  | **POST**  | AUTH   | Available |
| crafter.newDestructionRecipe(self, apiKey, otp, result, materials, counts) | **POST**  | OPEN   | Available |
| **Events**  |   |   |   |
| events.fetchEvents()  | **GET**  | OPEN   | Available |
| **Globals**  |   |   |   |
| globe.getMeta()  | **GET**  | OPEN   | Available |
| globe.getTokenAddress()  | **GET**  | OPEN   | Available |
| globe.newItem(apiKey, otp, name, id, totalSupply, metadata) | **POST**  | AUTH   | Available |
| **Items**  |   |   |   |
| items.getItems()  | **GET**  | OPEN   | Available |
| items.getItemAddresses()  | **GET**  | OPEN   | Available |
| items.ledger()  | **GET**  | OPEN   | Available |
| items.getItem(item)  | **GET**  | OPEN   | Available |
| items.getItemByAddress(item) | **GET**  | OPEN   | Available |
| items.spawnItem(item, useraccount) | **POST**  | OPEN   | Available |
| items.clearAvailability(item, useraccount) | **POST**  | OPEN   | Available |
| **LootBox** |   |   |   |
| lootbox.getChances()  | **GET**  | OPEN   | Available |
| lootbox.getCost()  | **GET**  | OPEN   | Available |
| lootbox.getItems(rarity)  | **GET**  | OPEN   | Available |
| lootbox.addItem(apikey, opt, item, rarity)  | **POST**  | AUTH  | Available |
| lootbox.updateChance(apikey, opt, epic,  rare, uncommon) | **GET**  | AUTH  | Available |
| lootbox.updateLootBoxCost(apikey, opt, cost)  | **GET**  | AUTH  | Available |

### Unit Tests

Run

```
cd unit
python -m unittest discover
```

inside the unit folder.
