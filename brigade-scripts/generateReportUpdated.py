#!/usr/bin/env python3
import requests
import json
import objectpath

name = "derek"
email = "pidgeotteam@gmail.com"
campsiteName = "bear"
URL = "https://ridb.recreation.gov/api/v1/campsites?query="+campsiteName+"&limit=5&offset=0"

print(URL)
data = {'accept': 'application/json', 'apikey': '77567128-da03-485c-b324-f8d2a0059b9d'}

r = requests.get(url = URL, params = data)
jsondata = r.json()
jsondata = json.dumps(jsondata)
jdata = json.loads(jsondata)

emailBodyToSend = "Dear INSERT_NAME_HERE, \n\n"
emailBodyToSend += "Here is your requested report on the campsites with the name INSERT_CAMPSITE_NAME_REQUEST_HERE: \n\n" 


for campsite in jdata['RECDATA']:
	emailBodyToSend += "Campsite Name: " + campsite.get('CampsiteName') + "\n"
	emailBodyToSend += "Campsite Longitude " + str(campsite.get('CampsiteLongitude'))+ "\n" 
	emailBodyToSend += "Campsite Latitude " + str(campsite.get('CampsiteLatitude')) + "\n"
	for attribute in campsite['ATTRIBUTES']:
		attributeName = attribute.get('AttributeName')
		if attributeName == 'Checkout Time':
			emailBodyToSend += "Checkout Time: " + attribute.get('AttributeValue') + "\n"
		if attributeName == 'Checkin Time':
			emailBodyToSend += "Checkin Time: " + attribute.get('AttributeValue') + "\n"

	emailBodyToSend += "\n"


emailBodyToSend += "Thanks,\n"
emailBodyToSend += "Team Pidgeot"

print(emailBodyToSend)


#campName = data['RECDATA'][0]
#Data to process from API:
#RECDATA
#       CampsiteName,
#       CampsiteType,
#       CampsiteLongitude,
#       CampsiteLatitude
#               Attributes:
#                       [AttributeName: "Toilet", AttributeValue: Y/N,
#                        AttributeName: "Checkout Time", AttributeValue: "11:00 AM",
#                        AttributeName: "Checkin Time", AttributeValue: "12:00 PM"]
