#!/usr/bin/env python3
import requests
import json
import objectpath
import sys
from datetime import datetime
from email.mime.text import MIMEText
import smtplib


info = json.loads(ascii(sys.argv[1].strip('b\'')).strip('\''))
name = info['Name']
email = info['email']
campsiteName = info['CampsiteName']

URL = "https://ridb.recreation.gov/api/v1/campsites?query="+campsiteName+"&limit=20&offset=0"

print(URL)
data = {'accept': 'application/json', 'apikey': '77567128-da03-485c-b324-f8d2a0059b9d'}

r = requests.get(url = URL, params = data)
jsondata = r.json()
jsondata = json.dumps(jsondata)
jdata = json.loads(jsondata)

emailBodyToSend = "Dear " + name + ", \n\n"
emailBodyToSend += "Here is your requested report on the campsites with the name " + campsiteName + ": \n\n" 


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

def exit():
    print("%sEmail script now exiting." % (current_timestamp()))

def current_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

# Email handling items - email addresses
ADMIN_NOTIFY_LIST = [email]
FROM_ADDRESS = 'pidgeotteam@gmail.com'

def send_server_status_report(message):
    # Init priority - should be NORMAL for most cases, so init it to that.

    # Init the send_mail flag.  Ideally, we would be sending mail if this function is
    # called, but we need to make sure that there are cases where it's not necessary
    # such as when there are no offline servers.
    send_mail = True

    if send_mail:
        body = """Report generated at: - %s 
        
        %s """ % (current_timestamp(), message)

        # craft msg base
        msg = MIMEText(body)
        msg['Subject'] = name + ", Report for campsite search of " + campsiteName   
        msg['From'] = FROM_ADDRESS
        msg['Sender'] = FROM_ADDRESS  # This is sort of important...

        # Initialize SMTP session variable so it has the correct scope
        # within this function, rather than just inside the 'try' statement.
        smtp = None

        try:
            # SMTP is important, so configure it via Google Mail.
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.ehlo()
            smtp.login(FROM_ADDRESS, 'fd67!pidgeot')
        except Exception as e:
            print("Could not correctly establish SMTP connection with Google, error was: %s" % (e.__str__()))
            exit()

        for destaddr in ADMIN_NOTIFY_LIST:
            # Change 'to' field, so only one shows up in 'To' headers.
            msg['To'] = destaddr

            try:
                # Actually send the email.
                smtp.sendmail(FROM_ADDRESS, destaddr, msg.as_string())
                print("%s  Email sent to [%s]." % (current_timestamp(), destaddr))
            except Exception as e:
                print("Could not send message, error was: %s" % (e.__str__()))
                continue

        # No more emails, so close the SMTP connection!
        smtp.close()
    else:
        print("%s  All's good, do nothing." % (current_timestamp()))

print(emailBodyToSend)
send_server_status_report(emailBodyToSend)


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
