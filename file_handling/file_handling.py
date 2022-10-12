#'w': Creates or rewrites a file.
with open('created_file', 'w') as file:
    file.write('This file was created using python.')

#'a' mode: Creates or attachs a file.

with open('created_file', 'a') as file:
    file.write('\nThis new line was created using append function on python.') #? '\n' is a line breaker.

with open('tree_file', 'w') as file:
    file.write('\n    /\   ')
    file.write('\n   /  \ ')
    file.write('\n  /    \ ')
    file.write('\n /______\ ')
    file.write('\n    ll  ')


with open('tree_file', 'a') as file:
    tree_string = '''\n
              X
             XXX
            XXXXXX
           XXXXXXXX
          XXXXXXXXXX
         XXXXXXXXXXXX
        XXXXXXXXXXXXXX
       XXXXXXXXXXXXXXXX
      XXXXXXXXXXXXXXXXXXX
     XXXXXXXXXXXXXXXXXXXXX
    XXXXXXXXXXXXXXXXXXXXXXX
             XXX
             XXX
             XXX
             XXX
    '''

    file.write(tree_string)
#'r' mode and read function: Reads what's inside of the file

with open('created_file', 'r') as file:
    print(file.read())

with open('tree_file', 'r') as file:
    print(file.read())

'''
    #* Explation

#! Open function basically opens a file and could take a 'mode' parameter too.

#! 1. I used 'w', 'a' and 'r' method to write a new file, append something on it and read it, respectively.
#! 2. I created two trees with strings. 
'''