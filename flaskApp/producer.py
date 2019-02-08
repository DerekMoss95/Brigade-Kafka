
from kafka import KafkaProducer
from kafka.errors import KafkaError
producer = KafkaProducer(bootstrap_servers=['192.168.70.3:9092'])#box 3, running kafka subscriber

def send(message):
    future = producer.send('pidgeot', message.encode())
    #producer.send('test', key=b'message-two', value=b'This is Kafka-Python')
    try:
        record_metadata = future.get(timeout=10) 
    except KafkaError:
        log.exception()
        pass

if __name__ == "__main__":
    send("test")
