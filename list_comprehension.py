chess_board = [[f'{let}{num}' for num in range(9) if num > 0] for let in 'ABCDEFGH'[::-1]]
    
for item in chess_board:
    print(item)


#! In this little project I did a chess board in python to understand list comprehension.

#* Concept:

#! 1 The f string appends the letter and the number to the list.
#! 2 The number goes untill 8 to make it increase in line.
#! 3 Beside it, the letter increase for each column.
#! 4 I used slicing to make the step negative to consequently inverse the order.