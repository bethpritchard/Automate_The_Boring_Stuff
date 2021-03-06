"""
Fantasy Game Inventory
"""


# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    """Prints contents and total number of items"""
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{k} {v}")
        item_total += v
    print("Total number of items: " + str(item_total))


"""
Dictionary to list 
"""


def addToInventory(inventory, addedItems):
    """ Adds items to dictionary """

    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
