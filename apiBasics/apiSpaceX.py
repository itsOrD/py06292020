#!/usr/bin/python3
"""
Authors:
    OP: RZFeeser
    Editor: itsOrD
This program harvests SpaceX data avail from https://api.spacexdata.com/v3/cores using the Python Standard Library methods
"""

# using std library method for getting at API data
import urllib.request 
import json
import time

# GOBAL / CONSTANT of the API we want to lookup
SPACEXURI = "https://api.spacexdata.com/v3/cores?pretty=true"

def main():
    # create a urllib.request response object by sending an HTTP GET to SPACEXURI
    coreData = urllib.request.urlopen(SPACEXURI)

    # pull STRING data off of the 200 response (even tho it's JSON!)
    xString = coreData.read().decode()
#    print(type(xString))

    # convert STRING data into Python Lists and Dictionaries
    listOfCores = json.loads(xString)
#    print(type(listOfCores))

    # core_serial
    for core in listOfCores:
        # TODO: utilize Python core to interpret/format API provided time
        launchDateTime = (core['original_launch'])
        print(core['core_serial'], ' - ',  launchDateTime, end='\n')

    # fString formatting
    for core in listOfCores:
        serial = core['core_serial']
        ldt = core['original_launch']
        print(f'SpaceX vehicle number: {serial} \n  launched on: {ldt}.', end='\n\n')

    # original_launch


#    for core in listOfCores:
#        print(core, end="\n\n")


if __name__ == "__main__":
    main()
