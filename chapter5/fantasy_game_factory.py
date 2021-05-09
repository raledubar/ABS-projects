#Fantasy game inventory
from typing import List, Dict, Tuple, Set, Callable
from pprint import pprint

stuff = {
    'rope': 1, 
    'torch': 6, 
    'gold coin': 42, 
    'dagger': 1,
    'arrow':  12
}

def display_inventory(inventory: dict()) -> int():
    print("inventory")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}\n")
        item_total += v
    print(f"total number of items: {item_total} ")

#display_inventory(stuff)

def add_to_inventory(inventory: Dict[str, int], added_items: List[str] ):
    for item_list in added_items:
             if item_list in inventory:
                 inventory[item_list] += 1
             else:
                 inventory[item_list] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
