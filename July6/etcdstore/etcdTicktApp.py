#!/usr/bin/python3
'''
Author: itsOrD
Description: learning about etcd by practicing with CRUD
             to make a 'ticketing' app
'''

import requests
import pprint

ETCD = 'http://127.0.0.1:2379/v2/keys/tickets'


def print2screen(resp):
    ## all functions need to have error checking and print to screen (for learning)
    resp = resp.json()
    if resp.get('errorCode'):
        print('Error present: ', resp['errorCode'])
        return False
    else:
        pprint.pprint(resp.json())


def getticks():
    ## user can query for tickets
    r = requests.get(ETCD)
    print2screen(r)


def getonetick(tickid):
    ## user can retrieve a ticket
    r = requests.get(f'''{ETCD}/{ticketid}''')
    print2screen(r)


def createtick(tickdata):
    ## user can create a ticket
    r = requests.put(f'''{ETCD}/{tickdata}''')
    print2screen(r)


def updatetick(ticketid):
    ## user can update a ticket
    r = requests.patch(ETCD, data=ticketid)
    print2screen(r)

def deleteticket(ticketid):
    ## user can delete a ticket
    r = requests.delete(ETCD, data=ticketid)
    print2screen(r)

def exit():
    ## user can exit the application
    return

def removeall():
    ## user can delete the entire collection
    r = requests.delete(ETCD)
    print('Deletion status: ', r.status_code)


if __name__ == '__main__':
    print('\n')
    getticks()
    createtick('lil')
    getonetick('tea')
    print('\n')
