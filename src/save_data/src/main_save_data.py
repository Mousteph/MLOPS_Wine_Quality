from consumer import ConsumerManager
import os

if __name__ == '__main__':
    servers_kafka = os.environ.get("SERVERS_K")
    topic_wine = os.environ.get("TOPIC_WINE")
    
    consumer = ConsumerManager([servers_kafka], topic_wine)
    consumer.start()
