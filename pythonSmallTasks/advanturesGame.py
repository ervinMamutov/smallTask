stuff = {'rope': 1, 'torch': 6, 'golden coint': 42, 'dagger': 1,
         'arrow': 12}

def displeyInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        item_total = inventory.get()
    print('Total inventory : ' + str(item_total))

displeyInventory(stuff)