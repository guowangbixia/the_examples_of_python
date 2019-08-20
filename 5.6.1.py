#a dict of game's goods
goods={'rope':1, 'torch': 6 ,'gold coin' : 42 ,'dagger':1 ,'arrow': 12}
def displayInventory(inventory):
    number=0
    for i in inventory.keys():
        print(str(inventory[i])+' '+i)
        number=number+inventory[i]
    return number
print('Inventory:')
print('Total number of items: '+str(displayInventory(goods)))

