#!/usr/bin/env python3

import base64
import requests

jamf_school_url = 'https://server.jamfcloud.com'


# to get Network ID go to Devices > Enroll Devices
network_id = '1234'
# To create API key go to "Organization" -> "Settings" -> "API"
api_key = 'XXXXXXXXX'



jamf_pro_auth = f'{network_id}:{api_key}'
jamf_pro_base64 = base64.b64encode(jamf_pro_auth.encode()).decode()


headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": f'Basic  {jamf_pro_base64}',
}

