FROM python:3.6.8-slim-jessie

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD server.py /
RUN chmod +x /server.py

ENTRYPOINT ["python3", "./server.py"]
