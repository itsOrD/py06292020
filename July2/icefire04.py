#!/usr/bin/python3
'''
Author: itsOrD
Description: fun with 'anapioficeandfire.com'
'''

import sys

import requests

IAF_API = 'https://www.anapioficeandfire.com/api/characters'


def main():
    ## get user input
    got_char_for_lookup = input(f''' What is the name of the character we're looking up? \n ''')
    
    ## send HTTPS GET to the API of ICE and FIRE char resource
    iaf_res = requests.get(f'''{IAF_API}?name={got_char_for_lookup}''')

    ## ensure validity
    if iaf_res.status_code != 200:
        sys.exit(f''' Your input '{got_char_for_lookup}' yielded no results.''')

    ## ensure json is present
    if iaf_res.json():
        iaf_rj = iaf_res.json()
    else:
        sys.exit(f''' The results for your input '{got_char_for_lookup}' are corrupted and can't be displayed''')

    ## print data for user
    print(f'''\n The character {got_char_for_lookup}'s URL is:  {iaf_rj[0]['url']}.''')

    ## determine char's allegiances
    if iaf_rj[0]['allegiances']:
        print(f''' {got_char_for_lookup}'s allegiances are: ''')
        for x in iaf_rj[0]['allegiances']:
            allegiance = requests.get(x)
            print(f'''  - {allegiance.json()['name']} ''')
    else:
        print(f''' {got_char_for_lookup} has no allegiances. ''')



if __name__ == "__main__":
    print('\n')
    main()
    print('\n\n')
