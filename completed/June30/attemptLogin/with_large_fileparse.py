#!/usr/bin/python3
'''
Author: itsOrD
Description: auto closing file parse
'''

def main():

    loginfails = 0
    list_loginfails_ip = []

    with open("/home/student/mycode/attemptLogin/keystone.common.wsgi") as kfile:
        for line in kfile:
            if "- - - - -] Authorization failed" in line:
                loginfails += 1
                list_loginfails_ip.append(line.split(' ')[-1])

    print(f'''Them fails be at: {loginfails}''')
    print(f'''The IPs to BAN are: ''')
    for ip in list_loginfails_ip:
#        print(lstrip('\n'))
        print(ip.rstrip('\n'), end=" ")

    print('\n')



if __name__ == "__main__":
    main()

