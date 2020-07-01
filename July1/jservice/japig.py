#!/usr/bin/python3
'''
Author: itsOrD
Description: write a 10 round 'Jeopardy Alexa'-ish game
             utilizing jservice.io
'''

import time

import requests


def main():
    '''game engine'''
    # non-op --> smile = u'\U0001f604'.encode('unicode-escape')
    smile = '\N{grinning face with smiling eyes}'
    print(f''' {smile} -- HELLO! AND WELCOME TO TOTALLY NOT A RIPOFF JEOPARDY! \n ''')
  
    username = input(f''' What's your name player? ''')
    print(f''' Welcome {username}. Let's get to the action ''')

    time.sleep(0.5)

    r = requests.get('https://jservice.io/api/random?count=3')
    rando_qs = r.json()
    qcnt = 0
    correct_ans_cnt = 0

    for x in rando_qs:
        print('\n')
        qcnt += 1
        ans = x.get('answer')
        if qcnt == 3:
            print(' FINAL JEOPARDY TIME! [this is the last question] ')
        print(f'''  Question {qcnt}: \n    "{x.get('question')}"''')
        user_ans = input()

        if user_ans == 'cheat':
            print(ans)
            user_ans = input()

        if compare_ans(user_ans, x):
            print('\n Correct!')
            correct_ans_cnt += 1
            print('your current score is --> ', correct_ans_cnt)

        else:
            print(f''' Sorry no... the answer was {ans}. ''')


    # end of game
    print(f''' \nAnd that's it for today's JEOPARDY ''')
    p_correct_ans_cnt = f'''\033[1;35;40m {correct_ans_cnt} \033[0m'''
    print(f''' Good game {username}.  You got {p_correct_ans_cnt} point out of a possible 3... ''')
    print('\n')
    high_score_check(username, correct_ans_cnt)
    print('\n')
    print(f''' JEOPARDY is now over. Run the file to play again with brand new questions! ''')


def compare_ans(ans_input, question_data):
    '''compares the user's input with the provided answer in a generous way'''
    correct_ans = question_data.get('answer')
    return (ans_input.lower() == correct_ans.lower())


def high_score_check(usr, score):
    '''writes usernames & high scores to external doc'''
    with open('jeopardyhighscores.txt') as hs:
        hs_list = hs.readlines()
        hs_len = 0

        if hs_list.len() < 10:
            hs.write(score)

        print('Your score has been recorded in the high scores list!')


if __name__ == "__main__":
    main()
    print('\n')
