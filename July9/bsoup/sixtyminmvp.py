#!/usr/bin/python3
''' itsOrD || scraping Alta3 with beautiful soup '''


from bs4 import BeautifulSoup
import requests


'''
=== From 'quick start' and experimentation ===
soup = BeautifulSoup("<p>Some<b>bad<i>HTML", features='lxml')
print(soup.prettify())
print('soup.find...', soup.find(text='bad'))
print('soup.i...', soup.i)

soup = BeautifulSoup("<tag1>Some<tag2/>bad<tag3>XML", "xml")
print(soup.prettify())
'''

ALTA = 'https://live.alta3.com/groups/evanescent-otters-strode/your-content' 


def main():
    # print from main
    delineate()
    firstAttempt()
    secondAttempt()
    thirdAttempt()
    fourthAttempt()
    delineate()
    

def firstAttempt():
    # scan alta3
    delineate(1)
    try:
        soup1 = BeautifulSoup(ALTA, features='lxml')
        print(soup1.prettify())
    except:
        print('You should learn more before you try to make your soup purty...')
    finally:
        print('\n')
        delineate(1)


def secondAttempt():
    delineate(2)
    # 'GET' the code that creates alta3 and scan it
    try:
        r = requests.get(ALTA)
        r = r.json()
    except:
        print('Cannot "GET" the page --> ', ALTA)
    try:
        soup2 = BeautifulSoup(r, features='lxml')
        print(soup2.prettify())
    except:
        print('Cannot make soup with .json from alta3... your soup remains ugly.')
    finally:
        print('\n')
        delineate(2)


def thirdAttempt():
    delineate(3)
    # understand the structure of alta3 and turn it into beautiful soup
    try:
        r = requests.get(ALTA)
        print(r.text)
        print(f'''\nThe content on '{ALTA}' is: \n TYPE : {type(r.text)}\n''')
        soup3 = BeautifulSoup(r.text, features='lxml')
        print(soup3.prettify())
    except:
        print('You kinda bad at soup beautifying...')
    finally:
        print('\n')
        delineate(3)


def fourthAttempt():
    delineate(4)
    # reach into the REACT app and make some soup
    try:
        r = requests.get('https://live.alta3.com/static/js/bundle.js')
        soup4 = BeautifulSoup(r.text, features='lxml')
        print(soup4.prettify())
    except:
        print('Thought that would work...')
    finally:
        print('\n')
        delineate(4)


def delineate(num = '='):
    # add spacing for quick visual grok of tests
    #print('\n')
    for i in range(37):
        print(f'''-{num}-''', end="")
    print('\n')


if __name__ == '__main__':
    main()
