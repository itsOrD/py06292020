#!/usr/bin/python3
'''
Author: itsOrD
Description: morning assignment, play with ISS API data
'''

import requests
import time
from time import ctime
# from geopy.distance import geodesic

def main():

    count = 0
    while count < 3:
        count += 1

        res = requests.get('http://api.open-notify.org/iss-now.json')

        if res.status_code != 200:
            print('GET request error. Non-200 error code returned')

        issData = res.json()
        issPos = issData.get('iss_position')

        lon = str(issPos['longitude'])
        lat = str(issPos['latitude'])

        timeStamp = time.ctime(issData.get('timestamp'))

        print(
                'ISS location on ' + timeStamp + 
                '\n latitude  :  ' + lat + 
                '\n longitude :  ' + lon
             )
        time.sleep(2)

# str(geodesic(ISSFinalPosition, amazonLocation).miles)

if __name__ == "__main__":
    main()

