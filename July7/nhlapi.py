#!/usr/bin/python3
'''
Author: itsOrD
Description: warm-up and practice with NHL API
'''

import requests

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


if __name__ == '__main__':
    print('\n')
    main()
    print('\n')
