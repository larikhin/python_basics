inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key


for k in inventory:
    print("Got key", k)


print(list(inventory.values()))

for v in inventory.values():
    print("Got", v)



print(list(inventory.items()))

for k, v in inventory.items():
    print("Got", k, "that maps to", v)

