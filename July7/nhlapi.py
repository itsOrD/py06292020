#!/usr/bin/python3
'''
Author: itsOrD
Description: warm-up and practice with NHL API
'''

import requests
import pandas as pd
from pandas.io.json import json_normalize

NHL = 'https://statsapi.web.nhl.com/api/v1/teams'


def main():
    # interactions with the API
    r = requests.get(NHL)
    r = r.json()
#    print(r)
    teams = r['teams']

    ## list all current teams
    print('---Current NHL teams---')
    for team in teams:
        tn = team.get('name')
        print(f''' TN {team.get('id')}: {tn}''')

    ## list active teams from league inception
    print('\n---NHL teams that have been active since season ONE---')
    for team in teams:
        yr = int(team.get('firstYearOfPlay'))
        if yr <= 1918:
            print(team.get('name') + ' - ' + str(yr))


    ## pandas practice
    pdd = pd.read_json(NHL)
   # print('pd.read_json(NHL): ', pdd)
    pdd_normalized = json_normalize(pdd['teams'])
   # print('json_normalized(pdd["teams"]): ', pdd_normalized)
    pddn_sorted = pdd_normalized.sort_values(by = ['id'])
   # print('pdd_normalized.sort_values(by = ["id"]): ', pddn_sorted)
    print(pdd_normalized.sort_values(by = ['firstYearOfPlay']).iloc[:51,[pdd_normalized.columns.get_loc("name"), pdd_normalized.columns.get_loc("firstYearOfPlay")]])



if __name__ == '__main__':
    print('\n')
    main()
    print('\n')
