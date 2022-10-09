stored_names = ['Candy', 'Meat', 'Vegetables', 'Drinks', 'Bread', 'Fish', 'Electronics', 'Canned food', 'Toys']
stored_numbers = [510, 2102, 2953, 987, 328, 84, 29, 874, 76]


for index, stocktaking in enumerate(zip(stored_names, stored_numbers)): 
    print(f'[ID {index}] - {stocktaking[0]}: {stocktaking [1]}') 


''' #* Explanation: 
#! 1 I used the zip method to merge both of the lists.
#! 2 With both of lists reduced to one, I used the enumerate method to give them an ID.
#! 2.1 The index value is assigned to each value of the stocktaking variable (returned as a tuple like below).
    #? Result: Now the result would be ({index}, ('name', num)).
#! 3 I printed it on a f string and telled to python how he should read it, first the name with [0] and [1] for the number.

#?? Final result:
    #* With both of the list merged with zip, the enumerate method on for loop gives an ID for each tuple of it, then:
        [ID 0] - Candy: 510
        [ID 1] - Meat: 2102
        ...
        [ID 8] - Toys: 76
'''
        

