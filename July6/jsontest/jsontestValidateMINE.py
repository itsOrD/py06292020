#!/usr/bin/python3
'''
Author: itsOrD
Description: playing with GET/POST and requests
'''

import requests
import json


H = 'http://'
URI = 'jsontest.com'


def main():
    ## pull ltimestamp of now
    dt_resp = requests.get(f'''{H}date.{URI}''')
    dt = dt_resp.json()
    dt = dt['date']
    print('DateTime: ', dt)

    ## pull current system IP
    ip_resp = requests.get(f'''{H}ip.{URI}''')
    ip = ip_resp.json()
    print('IP: ', ip['ip'])

    ## read in a list of servers from a file called myservers.txt
    ## TODO: mk file myservers.txt
    with open('myservers.txt', 'w') as servers:
        servers.write('host1\nhost2\nhost3')

    with open('myservers.txt', 'r') as serverfile:
        serverdata = serverfile.readlines()

    ## format the data in the following manner
    ## {"json": "time: <<PART A>>, ip: <<PARTB>>, mysvrs: [ <<PARTC>> ]"}
    mydata = {'json': {'time': dt, 'ip': ip, 'mysvrs': [serverdata]} }
    mydata_formatted = {"json": f"{{'time': {dt}, 'ip': {ip}, 'mysvrs': {serverdata}}}"}
 
    ## validate JSON with a POST
    v_resp = requests.post(f'''{H}validate.{URI}''', data=mydata_formatted)
    v = v_resp.json()
    print(v)
    print(f'''Is the JSON valid? --> {v['validate']}''')



if __name__ == '__main__':
    print('\n')
    main()
    print('\n')
