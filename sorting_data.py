stored_names = ['Candy', 'Meat', 'Vegetables', 'Drinks', 'Bread', 'Fish', 'Electronics', 'Canned food', 'Toys']
stored_numbers = [510, 2102, 2953, 987, 328, 84, 29, 874, 76]
combined_list = list(zip(stored_names, stored_numbers))

sorted_comp_let = sorted(combined_list, key = lambda stored_tuple: len(stored_tuple[0]))
sorted_comp_num = sorted(combined_list, key = lambda stored_tuple: stored_tuple[1])

print(sorted_comp_let)
print(sorted_comp_num)

''' 
    #* Explanation?

#! 1. I used stored method to order the combined list by their lenght and the amount of items, respectively.
#! 2. To sort by the name and by the amount, I used a lambda function to avoid making a small function in more lines than one.
#! 3. To sort the name I set a variable to make the lenght find the string and then this value is attached to the sorted method, making him search for the lenght of the words.
#! 4. To sort the number, I just set the index where the numbers are and then the sort method, as he searchs on an ascending way by default, pick the smaller one in first place. 
'''