FROM python:3.6.8-slim-jessie

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ENV topic 'pidgeot'
ENV host '192.168.70.3'
ENV port '9092'
ENV offset 'latest'
ENV brigade_project_name 'brigade-kafka'

ADD server.py /
RUN chmod +x /server.py
#What should I do here with giving server.py some arguments when it runs? Do i need to set ENVs? Or args? Or nothing and just handle it in the server.py argparse?
CMD [ "python3", "./server.py", "--topic='pidgeot'"]
