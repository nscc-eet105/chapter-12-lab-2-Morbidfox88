#Chad Collard
#Chapter 12 Lab 2
#7/11/2025
#The Unique Word Counter

print('Unique Word Counter\n')

import os

def unique_word_counter():
    file_name = ''
    while True:
        if not file_name:
            file_name = input('Enter the name of the file you wish to process: ')

        
        try:
            if not os.path.isfile(file_name):
                print(f'The file {file_name} could not be found!')
                


            with open(file_name, 'r') as file:
                content = file.read()
                content = content.lower()
                words = content.split()
                unique_words = set(words)
        
                print(f'There are {len(unique_words)} unique words in sample.txt\n')
                print('Thanks for using the program!')
                break

        
        except FileNotFoundError:
                file_name = input('Enter the name of the file you wish to process or type exit to quit ').lower()
                if file_name == 'exit':
                    print('\nThanks for using the program!')
                    break
                else:
                    continue
unique_word_counter()
