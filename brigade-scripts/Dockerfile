FROM python:3.6.8-slim-jessie

COPY requirements.txt .
COPY kafka-event.py /usr/local/bin/.

RUN chmod +x /usr/local/bin/kafka-event.py
RUN pip3 install -r requirements.txt

CMD python3 /usr/local/bin/kafka-event.py
