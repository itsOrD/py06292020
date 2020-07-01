#!/usr/bin/python3
'''
Author: itsOrD
Description: count failed login attempts via keystone
'''

# import keystone.common.wsgi

def main():

    failed_login_counter = 0

    k_file = open("/home/student/mycode/attemptLogin/keystone.common.wsgi", "r")

    k_file_lines = k_file.readlines()

    for line in k_file_lines:
        if '- - - - -] Authorization failed' in line:
            failed_login_counter += 1

    print(f'''Failed logins currently total: {failedLoginCounter}''')


    # TODO: same, but with regex
#    r_fail_count = 0
#    /- - - - -] Authorization failed/g
    

    print('''Via the mystical dark arts of regEx we can confirm there are "{r_fail_count}" failed logins''')


if __name__ == "__main__":
    main()

