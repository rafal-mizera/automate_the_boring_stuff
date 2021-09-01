stuff = {"sword": 2, "magic box": 1, "arrow": 10, "bow": 1}

def displayInventory(inventory):
    for item,number in inventory.items():
        print(f"{number} {item}")
    print(f"Your total items number: {len(inventory.keys())}")

displayInventory(stuff)

def addInventory(inventory,added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

new_items = ["sword", "arrow", "magic powder"]
addInventory(stuff,new_items)
displayInventory(stuff)