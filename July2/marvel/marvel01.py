#!/usr/bin/python3
'''
Author: itsOrD
Description: using Marvel's API to practice priv+pub API validation
'''

import argparse
import time
import hashlib

import requests


## API def
MARPI= 'http://gateway.marvel.com/v1/public/characters'

## Calculate the hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey_publicKey)
def hashbuilder(timeywimey, privkee, pubkee):
    return hashlib.md5((timeywimey + privkee + pubkee).encode('utf-8')).hexdigest()

## Perform the call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spier-Man&ts=1&apikey=1234&&hash=...
def marvelcharcall(stampy, hashy, pkeyz, look4me):
    r = requests.get(f'''{MARPI} 
