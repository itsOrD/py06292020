#!/usr/bin/python3
'''
Author: itsOrD
Description: this program will harvest data vail from 
https://api.spacexdata.com/v3/cores
using the Python Standard Library methods
'''

import urllib.request
import json

SPACEXURI = 'https://api.spacexdata.com/v3/cores'

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = urllib.request.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response
    xString = coreData.read().decode()

    print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)
    print(type(listOfCores))

    for core in listOfCores:
        print(core, end='\n\n')


if __name__ == "__main__":
    main()

