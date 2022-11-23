from consumer import ConsumerManager
import os
import time

if __name__ == '__main__':
    time.sleep(10)

    servers_kafka = os.environ.get("SERVERS_K")
    topic_succes = os.environ.get("TOPIC_SUCCESS")
    topic_error = os.environ.get("TOPIC_ERROR")
    
    consumer = ConsumerManager([servers_kafka], topic_succes, topic_error)
    consumer.start()
