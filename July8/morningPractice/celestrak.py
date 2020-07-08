#!/usr/bin/python3
''' itsOrD || tracking space objects in orbit via Pythonic API access '''


import requests


TRAK = 'https://www.celestrak.com/NORAD/elements/active.txt'


def main():
    # retrieve text list of objects
    r = requests.get(TRAK)
    # API provides data as txt instead of json...
   # r = r.json()
    with open('celestrakActiveElements.txt', 'w+') as localfile:
        localfile.write(r.text)
    print(r.text)


if __name__ == "__main__":
    print('\n')
    main()
    print('\n')
