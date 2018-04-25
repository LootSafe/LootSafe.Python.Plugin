# LootSafe.Python.Plugin

LootSafe API abstraction written in Python to aid developers with integrating LootSafe's services with their games.

Check out [our website](http://lootsafe.io/) for more information.

## Index

* [Requirements and Installation](#requirements-and-installation)
* [Running the example](#running-the-example)
* [Unit Tests](#unit-tests)
* [Endpoints](#endpoints)

## Requirements and Installation

Currently working on Python 3.6.4 running on Windows 10.

Imports used

* **sys**
* **unittest**
* **requests**
* **json**

Clone/Download this repository

Run

```
python setup.py install
```

All dependencies should be installed and we are ready to go!

## Running the example

Run the following command

```
python example.py
```

Contents of example

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

## Unit Tests

Keep in mind that some of the unit tests can clear availability 

**Configure the unit tests using**

```
unit/unit_config.py
```

**Running an individual test**

```
python -m unittest test_balance.py
```

**Running all tests**

```
python -m unittest discover
```

**Available Unit Tests**

```
test_balance.py
test_crafter.py
test_events.py
test_general.py
test_items.py
test_lootbox.py
```

## Endpoints

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
| **General**  |   |   |   |
| general.meta()  | **GET**  | OPEN   | Available |
| general.getTokenAddress()  | **GET**  | OPEN   | Available |
| general.newItem(apiKey, otp, name, id, totalSupply, metadata) | **POST**  | AUTH   | Available |
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

