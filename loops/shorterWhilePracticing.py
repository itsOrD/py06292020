#!/src/bin/python3
'''
Author: itsOrD
Description: Monty Python name guessing game to practice loops
'''

def main():
    round = 0
    answer = " "

    while round < 3 and answer != "Brian":
        round += 1
        answer = input('Finish the movie title, "Monty Python\'s The Life of ____": ')
        if answer.capitalize() == "Brian":
            print("Correct!")
            break;
        elif answer == "shrubbery":
            print("You've given the super-sekret answer! ...you... win?")
            break;
        elif round == 3:
            print("Sorry, the answer was Brian.")
        else:
            print("Sorry. Try again!")


if __name__ == "__main__":
    main()

