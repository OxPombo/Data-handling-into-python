print('Map & Filter')
print(' ')

map_filter_list = [1, 2, 3, 4, 5]

print(list(map(lambda num: num ** 2, map_filter_list)))
print(list(filter(lambda num: num < 4, map_filter_list)))

'''
    #* Explanation

#? Here I used the map and filter function to power the numbers of the list and also filter them.

#! 1. The map function walks in every number returning an iterator and power them through the lambda function.
#! 2. The filter function returns an iterator were their items are filtered through the lambda function.
'''

print(' ')
print('List comprehension')
print(' ')


print([num ** 2 for num in range(6) if num > 0])
print([num for num in range(6)[1:5] if num < 4 ])

'''
#! Testing list comprehension to get the same output
'''
