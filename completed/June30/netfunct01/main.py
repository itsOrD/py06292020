#!/usr/bin/python3
'''
Author: itsOrD
Description: function playtime
'''

# prints desired data to console
def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print(f'''\n Handshaking. .. ... connecting with {coffeetime} ''')
        for mycmds in devicecmd[coffeetime]:
            print(''' Attempting to send command --> {mycmds} ''')
    # kerning
    print('\n')

# psvm
def main():
    # this is the demo data that we're going to use to replace data stored in file
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":  
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 

    print(''' Welcome to the network device command pusher: \n''')

    ## get data set
    print(''' -Data set found- ''')  # replace with function call that reads in data from file

    ## run
    commandpush(work2do)  # call fxn to push commands to devices


if __name__ == "__main__":
    main()
