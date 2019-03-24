#!/usr/bin/python3

from flask import Flask
from flask import render_template
from flask import request
import json
import producer

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
        name = request.form['name']
        email = request.form['email']
        campsite = request.form['campsiteName']
        producer.send(json.dumps({'Name': name, 'email': email, 'CampsiteName': campsite}))
        return 'Recieved. Email will be sent once data is gathered'

if __name__ == "__main__":
    app.run(host= '0.0.0.0')



