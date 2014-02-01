#!/usr/bin/env python
"""Basic test of Sunlight API"""

import json as js
import requests
from pprint import pprint

# open settings file to retrieve API key
with open("conf/settings.json") as apifile:
    data = js.load(apifile)

# set custom header to use API key
headers = {'X-APIKEY': data['API']}

# API URL
url = 'https://congress.api.sunlightfoundation.com/'


# method to retrieve list of legislators
def legislators():
    r = requests.get(url + 'legislators', headers=headers)
    response = r.json()
    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of committees
def committees():
    r = requests.get(url + 'committees', headers=headers)
    response = r.json()
    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of bills
def bills():
    r = requests.get(url + 'bills', headers=headers)
    response = r.json()
    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of amendments
def amendments():
    r = requests.get(url + 'amendments', headers=headers)
    response = r.json()
    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of nominations
def nominations():
    r = requests.get(url + 'nominations', headers=headers)
    response = r.json()
    print '%d nominations' % response['count']
    pprint(response['results'][0])
    try:
        for item in response['results']:
            print item['nomination_id']
    except TypeError as err:
        print '%s' % err

#   print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of votes
def votes():
    r = requests.get(url + 'votes', headers=headers)
    response = r.json()
    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of updates from the floor
def floor_updates():
    r = requests.get(url + 'floor_updates', headers=headers)
    response = r.json()
    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of upcoming hearings
def hearings():
    r = requests.get(url + 'hearings', headers=headers)
    response = r.json()
    # parse the data to print only the description, time and location
    # of the hearing
    try:
        for item in response['results']:
            print item['description'], item['occurs_at'], item['room']
            print '\n'
    except TypeError as err:
        print '%s' % err
#    print js.dumps(response, sort_keys=True, indent=4)


# method to retrieve list of upcoming bills
def upcoming_bills():
    r = requests.get(url + 'upcoming_bills', headers=headers)
    upcoming = r.json()

    print 'The current number of upcoming bills is %d' % upcoming['count']
    print 'Listed below are the upcoming bills'
    print '=' * 35

    for i in upcoming['results']:
        print '\t' + i['bill_id']

    print '\n'

    #print js.dumps(r.json(), sort_keys=True, indent=4)


def main():
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
            if choice == 'l':
                legislators()
            elif choice == 'c':
                committees()
            elif choice == 'b':
                bills()
            elif choice == 'a':
                amendments()
            elif choice == 'n':
                nominations()
            elif choice == 'v':
                votes()
            elif choice == 'f':
                floor_updates()
            elif choice == 'h':
                hearings()
            elif choice == 'u':
                upcoming_bills()
            elif choice == 'q':
                break
            else:
                print 'Invalid selection. Try again or press q to quit'
                continue
        except KeyError:
            print 'Invalid selection. Try again or press q to quit'
            continue


if __name__ == '__main__':
    main()
