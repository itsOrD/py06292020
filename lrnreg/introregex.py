#!/usr/bin/python3
'''
Author: itsOrD
Description: intro to re (regular expressions) in Python
'''

import urllib.request
import re

def main():

    print(' Where should we search? ')

    url = input()

    print(f''' Mk... We'll try to open the url '{url}' and peform the search... ''')
    print(f''' But first! What's the phrase we're looking for? ''')

    searchFor = input()
    searchMe = urllib.request.urlopen(url).read().decode('utf-8')

    if re.search(searchFor, searchMe):
        print(' Found a match!')
    else:
        print(' Sry, no matches found.')


if __name__ == "__main__":
    main()

