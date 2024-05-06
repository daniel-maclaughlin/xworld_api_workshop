#!/usr/bin/env python3

import requests


jamf_pro_url = 'https://server.jamfcloud.com'

client_id = '720fc63b-4b3c-45d6-8a6e-XXXXXXXXXXX'
client_secret = '-3511nibgwd6-X3DOxkZ3Bzwa53vRC6Stoa3BBOXiQY_XXXXXXXXXXX'

headers = {
	"Content-Type": "application/x-www-form-urlencoded"
}

data = {
	"client_id": client_id,
	"grant_type": "client_credentials",
	"client_secret": client_secret
}
 

response = requests.post(f'{jamf_pro_url}/api/oauth/token', headers=headers, data=data)


jamf_pro_token = response.json()['token']

token_headers = {
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Authorization": f'Bearer {jamf_pro_token}'
}
