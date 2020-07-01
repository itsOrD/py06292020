#!/usr/bin/python3
'''
Author: itsOrD
Description: read IP adresses from user via ARGPARSE and return location
'''

import argparse
import requests

def main():
    '''
    ## from argparse docs:
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
            help='an integer for the accumulator')
    parser.add_argument('--sum
    '''
    # if the user passed in args.ip, then ipToLookUp auto-sets
    if args.ip:
        ipToLookUp = args.ip
    else:   # if the user did not pass a value via the --ip flag at the CLI
        ipToLookUp = input(f''' What is the IP address to lookup? ''')

    res = requests.get(f'''http://ip-api.com/json/{ipToLookUp}''')  # this sends an HTTP GET
    print(res.json())  # print out the JSON attached to the requests.get


# this is ONLY true if you run the script directly (i.e. python3 thisscript.py)    
if __name__ == "__main__":
    parser = argparse.ArgumentParser('')  # short descr of our program avail via help flag --help or -h
    parser.add_argument('--ip', help='The IP address to lookup via the API locator')
    args = parser.parse_args()
    main()

