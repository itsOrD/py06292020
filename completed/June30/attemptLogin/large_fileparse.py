#!/usr/bin/python3
'''
Auther: itsOrD
Description: preventing excessive memory load
             and ensuring doc is closed
'''

def main():

    loginfail = 0
    k_file = open("/home/student/mycode/attemptLogin/keystone.common.wsgi", "r")

    for line in k_file:
        if '- - - - -] Authorization failed' in line:
            loginfail += 1

    print(f'''Login fails: {loginfail}''')

    k_file.close()



if __name__ == "__main__":
    main()

