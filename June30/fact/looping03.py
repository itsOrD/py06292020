#!/usr/bin/python3
'''
Author: itsOrD
Description: UUID creation with range()
'''

import uuid

def main():

    howmany = int(input("How many UUIDs should be generated? "))

    print("Generating UUIDs...")

    for rando in range(howmany):
        print( uuid.uuid4() )



if __name__ == "__main__":
    main()
