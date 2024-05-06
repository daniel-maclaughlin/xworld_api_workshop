#!/bin/bash

#source server
jamf_pro_url="https://server.jamfcloud.com"


client_id="720fc63b-4b3c-45d6-8a6e-XXXXXXXXXXX"
client_secret="-3511nibgwd6-X3DOxkZ3Bzwa53vRC6Stoa3BBOXiQY_XXXXXXXXXXX"

getJsonValue() {
	# You can pass some json and a key into this function and get back the value
	# $1=json string, $2=key to return
	# e.g., json='{"key": "value"}'; val=getJsonValue "$json" "key"; echo $val => "value"
	JSON="$1" osascript -l 'JavaScript' \
	-e 'const env = $.NSProcessInfo.processInfo.environment.objectForKey("JSON").js' \
	-e "JSON.parse(env).$2"
	#	EndOfScript
}


#oauth token
oauth_token=$(curl -X POST \
${jamf_pro_url}/api/oauth/token \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode "client_id=${client_id}" \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode "client_secret=${client_secret}")
echo ${oauth_token}


api_token=$( getJsonValue "${oauth_token}" "access_token" )
echo ${access_token}

# activation code
activation_code=$(curl -X GET \ 
${jamf_pro_url}/JSSResource/activationcode \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer  ${api_token}")
echo ${activation_code}
