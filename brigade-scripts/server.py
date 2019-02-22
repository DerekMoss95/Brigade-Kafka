from kafka import KafkaConsumer
import kafkaEvent

consumer = KafkaConsumer('pidgeot', bootstrap_servers='192.168.70.3:9092', auto_offset_reset='latest')

if __name__ == '__main__':
    for message in consumer:
        # reset these global variables on every run
        print (message)
        messagestr = message.value
        kafkaEvent.createSecretPython(messagestr)
        #time.sleep(180)
