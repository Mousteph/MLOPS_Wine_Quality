from kafka import KafkaProducer
import json
from typing import List
import time

class PredictionProducer:
    def __init__(self, servers: List, topic_wine: str):
        self.servers = servers
        self.topic_wine = topic_wine
        
        is_ok = False
        producer = None
        repeat = 20

        while not is_ok and repeat != 0:
            try: 
                producer = KafkaProducer(
                        bootstrap_servers=servers,
                        value_serializer=lambda data: json.dumps(data).encode('utf-8')
                    )
                is_ok = True
            except Exception as _:
                time.sleep(2)
                repeat -= 1
                
        if repeat == 0:
            raise RuntimeError("Cannot connect to Kakfa broker")

        self.producer = producer

    def produce_wine(self, x, y):
        message = {
            "X": x,
            "y": float(y) if y is not None else None
        }
        
        self.producer.send(self.topic_wine, message)
        self.producer.flush()