#!/bin/bash

#source server
jamf_pro_url="https://server.jamfcloud.com"

api_user="jssadmin"
api_password='password'


getJsonValue() {
	# You can pass some json and a key into this function and get back the value
	# $1=json string, $2=key to return
	# e.g., json='{"key": "value"}'; val=getJsonValue "$json" "key"; echo $val => "value"
	JSON="$1" osascript -l 'JavaScript' \
	-e 'const env = $.NSProcessInfo.processInfo.environment.objectForKey("JSON").js' \
	-e "JSON.parse(env).$2"
	#	EndOfScript
}


#getting Universal API token
#get token for UAPI communication
bearer_token=$(curl -X POST \
${jamf_pro_url}/uapi/auth/tokens \
--header 'Content-Type: application/json' \
--user "${api_user}:${api_password}")
echo ${bearer_token}



api_token=$( getJsonValue "${bearer_token}" "token" )
echo ${api_token}


# activation code
activation_code=$(curl -X GET \ 
${jamf_pro_url}/JSSResource/activationcode \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header "Authorization: Bearer  ${api_token}")
echo ${activation_code}
