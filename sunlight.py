#!/usr/bin/env python
"""Basic test of Sunlight API"""

import json as js
import requests

with open("conf/settings.json") as apifile:
    data = js.load(apifile)

headers = {'X-APIKEY': data['API']}

url = 'https://congress.api.sunlightfoundation.com/'


methods = {'l': 'legislators', 'c': 'committees', 'b': 'bills',
           'a': 'amendments', 'n': 'nominations', 'v': 'votes',
           'f': 'floor_updates', 'h': 'hearings',
           'u': 'upcoming_bills'}

while True:
    menu = """ Please select one of the following:
                01. (l)egislators
                02. (c)ommittees
                03. (b)ills
                04. (a)mendments
                05. (n)ominations
                06. (v)otes
                07. (f)loor updates
                08. (h)earings
                09. (u)pcoming bills
                10. (q)uit
"""
    choice = raw_input(menu + '\n>')
    try:
        if choice == 'q':
            break
        else:
            r = requests.get(url + methods[choice], headers=headers)
            response = r.json()
            print js.dumps(response, sort_keys=True, indent=4)
    except KeyError:
        print 'Invalid selection. Try again or press q to quit'
        continue


def legislators():
    pass


def committees():
    pass


def bills():
    pass


def amendments():
    pass


def votes():
    pass


def floor_updates():
    pass


def hearings():
    pass


def upcoming_bills():
    r = requests.get(url + 'upcoming_bills', headers=headers)
    upcoming_bills = r.json()

    print 'The current number of upcoming bills is %d' % upcoming_bills['count']
    print 'Listed below are the upcoming bills'
    print '=' * 35

    for i in upcoming_bills['results']:
        print '\t' + i['bill_id']

    print '\n'

    print js.dumps(r.json(), sort_keys=True, indent=4)


if __name__ == '__main__':
    pass
