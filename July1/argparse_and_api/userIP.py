#!/usr/bin/python3
'''
Author: itsOrD
Description: interact with user and perform IP lookup
'''

import requests
import time

def main():

    print('\n')

    u_ip = input(' --Thank you for running "UserIP" - what IP can we physically locate for you today?-- \n ')
    
    print(f''' Got it, locating {u_ip} now...''')

    res = requests.get(f'''http://ip-api.com/json/{u_ip}''')
    ip_info = res.json()

    time.sleep(1)
    print(' . ')
    time.sleep(1)
    print(' .. ')
    time.sleep(1)
    print(' ... ')
    time.sleep(1)
    print(f''' {u_ip} is located in: '''.rstrip('\n'))
    time.sleep(1)
    print(f'''   {ip_info.get('city')}, {ip_info.get('country')} ''')

    print('\n')


if __name__ == "__main__":
    main()
