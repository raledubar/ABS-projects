#Fantasy game inventory
from pprint import pprint

stuff = {
    'rope': 1, 
    'torch': 6, 
    'gold coin': 42, 
    'dagger': 1,
    'arrow':  12
}

def display_inventory(inventory):
    print("inventory")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}\n")
        item_total += v
    print(f"total number of items: {item_total} ")

display_inventory(stuff)