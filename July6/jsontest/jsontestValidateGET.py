#!/usr/bin/python3
'''
Author: itsOrD
Description: learning GET utilzing requests libray
'''

import requests
import json


GETURL = 'http://validate.jsontest.com/'


def main():
    # tet data to validate as legal json
    mydata = {'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}
    
    ## the next two lines do the same thing
    ## we take python, convert to a string, then strip out whitespace
    #jsonToValidate = "json=" + str(mydata).replace(" ", "")
    #jsonToValidate = f"json={ str(mydata).replace(' ', '') }"
    ## slightly different thinking
    ## user json library to convert to legal json, then strip out whitespace
    jsonToValidate = f'''json={ json.dumps(mydata).replace(' ', '') }'''

    # use requests library to send an TTP GET
    resp = requests.get(f'''{GETURL}?{jsonToValidate}''')
    respjson = resp.json()
    print(respjson)

    # JUST display the value of 'validate'
    print(f'''Is your JSON valid? {respjson['validate']}''')


if __name__ == '__main__':
    print('\n')
    main()
    print('\n')
