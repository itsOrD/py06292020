#!/usr/bin/python3
''' 
Author: itsOrD
Description: write a python script that accepts an IPv4 address from the user,
and returns where that IP address is in the worlod along with any other
'''

import requests

def main():

    with open("ipv4data.txt", "a") as ipData:
        for x in range(10):
            res = requests.get(f'''http://ip-api.com/json/{x}2.{x}2.0.{x}''')
#            indiv_ip = res.json()
            ipData.write(res.text + '\n\n')



if __name__ == "__main__":
    main()

