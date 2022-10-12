# creating lists (could be anything) to del, remove, pop and clear, respectively.

my_list_del = [1, 2, 3, 4, 5]
my_list_rem = [15, 18, 30, 40]
my_list_pop = [33, 44, 55, 66]
my_list_cl = [41295128512610682908607234832, 8156296230302692, 18351691350, 9]

#! del keyword: Deletes the thing you're poining with index or just exludeds everything.

print('Del keywor:d')
del my_list_del[4]
print(my_list_del)

del(my_list_del) # Now, I can't do anything with it, because it simple doesn't exist.

#! remove method: Removes an item, specified with value.

print(' ')
print('Remove method:')

my_list_rem.remove(18)
print(my_list_rem)

#! pop method: Pops out the item of a container, but pointing with negative index.

print(' ')
print('Pop method:')

print(my_list_pop)
print(my_list_pop.pop(-1)) # Prints the removed item.

#! clear method: Clears all the stuff of a object.

print(' ')
print('Clear method:')

my_list_cl.clear()
print(my_list_cl)