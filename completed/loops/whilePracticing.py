#!/usr/bin/python3
'''
Author: itsOrD
Description: practicing while loops and if-else
'''

def main():
    round = 0
    
    while True:
        round = round + 1
        print('Finish the movie title, "Monty Python\'s The Life of ___"')

        answer = input('Your guess --> ')
        if answer == 'Brian':
             print('Correct!')
             break
        elif round == 3:
             print('Sorry, the answer was Brian.')
             break
        else:
             print('Sorry. Try again!')

        
    print('The loop has ended!')


# script engine
if __name__ == "__main__":
    main()

