#!/usr/bin/python3
'''
Author: itsOrD
Description: playground for Python API integration
             learning - utilizing SpaceX API
'''

import requests

# integrate API data and print dictionaries
def main():
    response = requests.get('https://api.spacexdata.com/v3/capsules')

    ## print entire endpoint 'body' (aka 'text')
#    print(response.text)

    ## print a list of just the capsule_serial
    for capsule in response.json():
        print(capsule.get('capsule_serial'))


# script engine
if __name__ == "__main__":
    main()


#'''
#import json
#
#with open('spacex.data', 'r') as jsonfile:
#    spacexdata = json.load(jsonfile)  # use the json library to LOAD our json data into python
#                                     # this causes python to recognize the lists
#...
#
#'''
                                    

