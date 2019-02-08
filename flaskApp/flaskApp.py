from flask import Flask
from flask import render_template
from flask import request
import producer

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
        nationPark = request.form['parkName']
        startDate = request.form['startDate']
        endDate = request.form['endDate']
        producer.send(nationPark + startDate + endDate)
        return 'OK'

if __name__ == "__main__":
    app.run(host= '0.0.0.0')



