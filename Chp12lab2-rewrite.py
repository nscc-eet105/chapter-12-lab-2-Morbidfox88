#Chad Collard
#Chapter 12 Lab 2
#7/11/2025
#The Unique Word Counter

print('Unique Word Counter\n')

import os

def unique_word_counter():
    file_name = input('Enter the name of the file you wish to process: ').lower()
    while not file_name or file_name != "exit":
        if not os.path.isfile(file_name):
            print(f'The file {file_name} could not be found!')
            file_name = input('Enter the name of the file you wish to process or type exit to quit ').lower()
        # The statements below the else only run if the file DOES exist
        else:
            with open(file_name, 'r') as file:
                content = file.read()
            content = content.lower()
            words = content.split()
            unique_words = set(words)
            print(f'There are {len(unique_words)} unique words in {file_name}\n')
            # Set file_name to "exit" so the program ends the next time the loop condition is checked
            file_name = "exit"
    print('Thanks for using the program!')
            
unique_word_counter()
