#!/usr/bin/python3
'''
Author: itsOrD
Description: learning about using keys with API's
             while using Python
'''

import urllib.request
import json

import webbrowser


NASAAPI = 'https://api.nasa.gov/planetary/apod?'


def main():

    ## Define credentials
    with open('/home/student/.keys/nasa_creds') as mycreds:
        nasacred = mycreds.read()

    ## remove an "extra" new line feeds on our key (just in case)
    nasacred = 'api_key=' + nasacred.strip('\n')

    ## call the webservice with our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacred)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode JSON to useful Python data structure
    apod = json.loads(apodread.decode('utf-8'))

    ## desiplay our Pythonic data
    print('\n\n --Converted Python Data-- ')
    print(apod)
    print(apod['title'], '\n')
    print(apod.get('data'), '\n')
    print(apod['explanation'], '\n')
    print(apod['url'])

    ## check out the result in a browser
    input('\n Press enter to open NASA pic of the day in browser')
    webbrowser.open(apod['url'])


if __name__ == "__main__":
    main()
