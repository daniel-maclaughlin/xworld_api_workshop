#!/usr/bin/env python3

import base64
import requests


jamf_pro_url = 'https://server.jamfcloud.com'

api_username = 'jssadmin'
api_password = 'password'



jamf_pro_auth = f'{api_username}:{api_password}'
jamf_pro_base64 = base64.b64encode(jamf_pro_auth.encode()).decode()


headers = {
	"Content-Type": "application/json",
	"Authorization": f'Basic  {jamf_pro_base64}',
}

response = requests.post(f'{jamf_pro_url}/uapi/auth/tokens', headers=headers)
print(response.status_code)
print(response.json())