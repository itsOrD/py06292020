#!/usr/bin/python3
''' itsOrD || logging behavior of API '''

import logging 
import argparse
import pprint
import requests


BOOK = 'https://www.anapioficeandfire.com/api/books'


def main():
    # if you use logging, ALWAYS describe your logging.basicConfig @ the start
    # default logging level is 'warning', which would skip less severe warnings
    logging.basicConfig(filename='icefire.log', format='%(levelname)s:%(asctime)s %(message)s',\
            datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    
    try:
        # this writes
        # INFO: 12/12/2019 11:55:02 AM Scripting started
        logging.info('Scripting started')

        # make a call to the API
        icefire = requests.get(BOOK + '/' + args.bookno)
        
        # force a ZeroDivisionError
        # 10 / 0

        # pretty print the json resp
        pprint.pprint(icefire.json())

        # write response code to log
        logging.info('API Resp code: ', str(icefire.code))

    # if a program errors, write that error to a log fiel
    except Exception as err:
        logging.critical(err)

    finally:
        # INFO:12/12/2019 11:55:02 AM Program endeded
        logging.info(' -- Program endeded')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bookno', help='Enter the book number (as an integer) to look it up.')
    args = parser.parse_args()
    main()
