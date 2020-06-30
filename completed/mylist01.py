#!/usr/bin/python3
# doc string goes here
'''
Author: ...
Definitions: ...
i'm a multi-line
string
comment. aren't I so cool!
'''

# all code should live inside of a function
# and should NOT be boiler-plate (left justified)
def main():
    '''
    best practice is to have
    another multi-line comment
    describing upcoming schtuff
    '''
    movies = []  # one-way to create a list
    movies.append("Big Hero 6")  # .append is a list method that applies the value
                                # passed to it at the END of the list

    movies.append("DieHard")

    print(movies)  # use the print FUNCTION to display to std out

    # ['Big Hero 6', 'DieHard']
    print(movies[0])

    movies.append("Saturday Night Lights")  # add SNL to the end of the list

    # print that newly added (end of list) item
    print(movies[2])
    print(movies[-1])
    print(movies[movies.index("Saturday Night Lights")])

# Zach says this is the "best" way to run the main function
# a major caveat to that is when importing code from another file
if __name__ == "__main__":
    main()

