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
print(type(jsondata))

print(jsondata.get("CampsiteName"))


jsondata = json.dumps(jsondata)
jdata = json.loads(jsondata)

print(jdata['RECDATA'][0]['ATTRIBUTES'][0]['AttributeName'])

#jdata['CampsiteName']



#tree_obj = objectpath.Tree(jsondata)
#print(tuple(tree_obj.execute('$..CampsiteName')))



#campName = data['RECDATA'][0]
#Data to process from API:
#RECDATA
#	CampsiteName,
#	CampsiteType,
#	CampsiteLongitude,
#	CampsiteLatitude
#		Attributes:
#			[AttributeName: "Toilet", AttributeValue: Y/N,
#			 AttributeName: "Checkout Time", AttributeValue: "11:00 AM",
#			 AttributeName: "Checkin Time", AttributeValue: "12:00 PM"]
#

#campsiteName = jsondata['RECDATA'][0]['CampsiteName']
#toilet = jsondata['RECDATA'][0]['ATTRIBUTES'][0]['AttributeName'] 
#toiletValue = jsondata['RECDATA'][1]['ATTRIBUTES'][0]['AttributeValue']
#checkout = jsondata['RECDATA'][0]['ATTRIBUTES'][8]['AttributeValue']
#checkin = jsondata['RECDATA'][0]['ATTRIBUTES'][16]['AttributeValue']


#print(campsiteName)
#print(toilet)
#print(toiletValue)


#print(jsondata)
