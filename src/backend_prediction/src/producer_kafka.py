from kafka import KafkaProducer
import json
from typing import List
import time

class PredictionProducer:
    def __init__(self, servers: List, topic_success: str, topic_error: str):
        self.servers = servers
        self.topic_success = topic_success
        self.topic_error = topic_error
        
        time.sleep(10) # Wait to kafka to launch
        
        self.producer = KafkaProducer(
                bootstrap_servers=servers,
                value_serializer=lambda data: json.dumps(data).encode('utf-8')
            )

    def produce_success(self, x, y):
        message = {
            "X": x,
            "y": y
        }
        
        self.producer.send(self.topic_success, message)
        # self.producer.flush()
        
    def produce_error(self, x, msg):
        message = {
            "X": x,
            "msg": msg
        }
        
        self.producer.send(self.topic_error, message)
        # self.producer.flush()
