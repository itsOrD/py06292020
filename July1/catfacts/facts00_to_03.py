#!/usr/bin/python3
'''
Author: itsOrD
Description: API/JSON learning with catfacts
'''

import requests


def main():
    '''Run tim code'''
    r = requests.get('https://cat-fact.herokuapp.com/facts')

    ## available methods in 'requests'
#    print( dir(r) )
    '''
   # yields the following:
   ['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']
   '''

#    print( r.json() )

#    print('\n\n\n')

    ## if we request the 'all' key, we can strip off the outside {}
#    print( r.json().get('all') )
    
#    for catfact in r.json()['all']:
#        print(catfact.get('text'))

   ## practice using additional methods in 'requests' revealed by print( dir(r) ) above
   



if __name__ == "__main__":
    main()
