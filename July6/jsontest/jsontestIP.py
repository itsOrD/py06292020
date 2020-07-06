#!/usr/bin/python3

import requests

IPURL = 'http://ip.jsontest.com/'


def main():
    # use requests libary to send an HTTP GET
    resp = requests.get(IPURL)
    #strip off JSON respons and convert to PYTHON LIST/DICT
    respjson = resp.json()
    # display our PYTHONIC data
    print(respjson)
    
    # display only value of 'ip'
    print(f'''The current WAN IP is --> {respjson['ip']}''')
    
    
if __name__ == "__main__":
    print('\n')
    main()
    print('\n')
