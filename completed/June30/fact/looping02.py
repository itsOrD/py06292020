#!/usr/bin/python3

def main():
    '''
    dnsfile = open("dnsservers.txt", "r")

    dnslist = dnsfile.readlines()

    for svr in dnslist:
        print(svr, end="")

    dnsfile.close()
    '''

    '''
    # take 2
    with open("dnsservers.txt", "r") as dnsfile:
        dnslist = dnsfile.readlines()

        for svr in dnslist:
            print(svr, end="")
    '''
    # take 3
    with open("dnsservers.txt", "r") as dnsfile:
        for svr in dnsfile:
            print(svr, end="")

    # conditionally create new docs 
    with open("dnsservers.txt", "r") as dnsfile:
        for svr in dnsfile:
            svr = svr.rstrip('\n')
            if svr.endswith('.org'):
                with open("org-domain.txt", "a") as orgfile:
                    orgfile.write(svr + '\n')
            elif svr.endswith('.com'):
                with open("com-domain.txt", "a") as comfile:
                    comfile.write(svr + '\n')

if __name__ == "__main__":
    main()

