#!/usr/bin/env python

import requests
import sys
import traceback
import time
import json
from .anilist_config import aniclient, anisecret

ANICLIENT = aniclient
ANISECRET = anisecret

# Leave this variable alone, go to anilist_config.py
access_token = ''

def usage():
    print('usage: anilist.py <anilist_id> <manga|anime>')
    sys.exit(2)

def check_and_get_old_token():
    try:
        # open the file if it exists
        print('Checking for token file')
        token_file = open('anilist.token', 'r+')
        token_json = json.load(token_file)
        time_now = time.time()

        if time_now < token_json['expires']:
            global access_token
            access_token = token_json['access_token']
            token_file.close()
            print('Token file checked and valid')
            return True
        else:
            token_file.close()
            print('Token file checked and invalid')
            return False

    except Exception as e:
        # Token file doesnt exist or there was some other error
        # create a new empty token file
        print('No existing token file found')
        open('anilist.token', 'w').close()
        return False

def get_new_token():
    try:
        print ('Trying to get new anilist token')
        request = requests.post('https://anilist.co/api/auth/access_token', params={'grant_type':'client_credentials', 'client_id':ANICLIENT, 'client_secret':ANISECRET})
        print ('Gained anilist token')

        print('Writing new anilist token file')
        request_json = request.json()
        f = open('anilist.token', 'w')
        json.dump(request_json, f)
        f.close()

        global access_token
        access_token = request_json['access_token']
    except Exception as e:
        traceback.print_exc()
        print('Error getting anilist API token')

def setup():
    if check_and_get_old_token():
        return
    else:
        print('No valid existing token file')
        get_new_token()

def get_info(media_id, media_type):
    url = 'https://anilist.co/api/'
    if media_type == 'anime':
        url += 'anime/'
    elif media_type == 'manga':
        url += 'manga/'
    else:
        usage()

    try:
        request = requests.get(url+ str(media_id), params={'access_token':access_token})

        if request.status_code == 401:
            setup()
            request = requests.get(url + str(media_id), params={'access_token':access_token})
        
        if request.status_code == 200:
            return request.json()
        else:
            return None
    except Exception as e:
        traceback.print_exc()
        return None

def main():
    args = len(sys.argv)
    if (args < 3) or (args > 4):
        usage()

    media_info = get_info(sys.argv[1], sys.argv[2])

    print('\nOUTPUT:\n')

    if not media_info:
        print ('Series does not exist')
    else:
        print(media_info['title_romaji'] + '\n')
        print(media_info['description'] + '\n')
main()
