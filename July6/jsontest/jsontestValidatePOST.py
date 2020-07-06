#!/usr/bin/python3
'''
Author: itsOrD
Description: using requests library to learn about POSTs
'''


import requests


POSTURL = 'http://validate.jsontest.com/'


def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }

    # send POST with data
    resp = requests.post(POSTURL, data=mydata)
    respjson = resp.json()
    print(respjson)

    print(f'''Is your JSON valid? {respjson['validate']}''')


if __name__ == '__main__':
    main()
