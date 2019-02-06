#!/usr/bin/env python

import socket
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import atexit
import ssl
import time 
import os
from kafka import KafkaConsumer

consumer = KafkaConsumer('pidgeot-test', bootstrap_servers='192.168.70.3:9092', auto_offset_reset='latest')

# #### VARIABLES #### #

# list of servers to check with the following items in the
# definitions per-server: ('hostname', 'ssl or plain', portnumber)

#host_ip = os.environ['HOST_IP']
#host_username = os.environ['USERNAME']
#print(host_ip)

# Email handling items - email addresses
ADMIN_NOTIFY_LIST = ['mossderek88@gmail.com', 'pidgeotteam@gmail.com']
FROM_ADDRESS = 'pidgeotteam@gmail.com'

# Begin Execution Here

def exit():
    print("%sEmail script now exiting." % (current_timestamp()))

def current_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def send_server_status_report(message):
    # Init priority - should be NORMAL for most cases, so init it to that.

    # Init the send_mail flag.  Ideally, we would be sending mail if this function is
    # called, but we need to make sure that there are cases where it's not necessary
    # such as when there are no offline servers.
    send_mail = True

    if send_mail:
        body = """Sent an email! - %s 
        
        %s """ % (current_timestamp(), message)

        # craft msg base
        msg = MIMEText(body)
        msg['Subject'] = "Report - %s" % (current_timestamp()) 
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


def main(messagestr):
    send_server_status_report(messagestr)  # Create email to send the status notices.
    exit()  # Exit when done


if __name__ == "__main__":
    print("%s  Server Status Checker Running...." % (current_timestamp()))
    for message in consumer:
        # reset these global variables on every run
        print (message)
        messagestr = message.value
        main(messagestr)
        #time.sleep(180)
