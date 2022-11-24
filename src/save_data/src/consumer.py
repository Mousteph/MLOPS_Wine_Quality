from kafka import KafkaConsumer
import json
from typing import List
from postgresql import manager
import time

class ConsumerManager:
    def __init__(self, servers: List, topic_success: str, topic_error: str):
        self.servers = servers
        self.topic_success = topic_success
        self.topic_error = topic_error
        
        is_ok = False
        consumer_data = None
        repeat = 20

        while not is_ok and repeat != 0:
            try: 
                consumer_data = KafkaConsumer(
                    value_deserializer=lambda data: json.loads(data.decode('utf-8')),
                    bootstrap_servers=self.servers
                )
                consumer_data.subscribe(topics=[self.topic_success, self.topic_error])
                is_ok = True
            except Exception as _:
                time.sleep(2)
                repeat -= 1
                
        if repeat == 0:
            raise RuntimeError("Cannot connect to Kakfa broker")
        
        self.consumer_data = consumer_data
        self.postgres_db = manager.ManagerPostgres()
        
    def start(self):
        for message in self.consumer_data:
            data = message.value
            if message.topic == self.topic_success:
                self.postgres_db.add_new_prediction(data["X"], data["y"])
