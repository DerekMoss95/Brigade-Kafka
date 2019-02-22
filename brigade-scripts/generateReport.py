#!/usr/bin/env python3
import requests

name = "derek"
email = "pidgeotteam@gmail.com"
campsiteName = "bear"
URL = "https://ridb.recreation.gov/api/v1/campsites?query="+campsiteName+"&limit=5&offset=0"

print(URL)
data = {'accept': 'application/json', 'apikey': '77567128-da03-485c-b324-f8d2a0059b9d'}

r = requests.get(url = URL, params = data)
jsondata = r.json() 

#campName = data['RECDATA'][0]

print(jsondata)