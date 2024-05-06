#!/usr/bin/env python3

import base64
import requests


jamf_pro_url = 'https://thegrid.jamfcloud.com'

api_username = 'jssadmin'
api_password = 'J@mf246810!'



jamf_pro_auth = f'{api_username}:{api_password}'
jamf_pro_base64 = base64.b64encode(jamf_pro_auth.encode()).decode()


headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": f'Basic  {jamf_pro_base64}',
}

response = requests.post(f'{jamf_pro_url}/uapi/auth/tokens', headers=headers)

jamf_pro_token = response.json()['token']

token_headers = {
	"Content-Type": "application/json",
	"Accept": "application/json",
	"Authorization": f'Bearer {jamf_pro_token}'
}
