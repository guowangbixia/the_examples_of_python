def addToInventory(inventory,addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory
def displayInventory(inventory):
    number=0
    for i in inventory.keys():
        print(str(inventory[i])+' '+i)
        number=number+inventory[i]
    print('Total number of items: '+str(number))
print('Inventory:')
inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin', 'dagger' ,'gold coin', 'gold coin' ,'ruby']
inv=addToInventory(inv,dragonLoot)
displayInventory(inv)
