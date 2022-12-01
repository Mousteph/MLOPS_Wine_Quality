from kafka import KafkaConsumer
import json
from typing import List
from postgresql import manager
import time

class ConsumerManager:
    def __init__(self, servers: List, topic_wine: str):
        self.servers = servers
        self.topic_wine = topic_wine
        
        is_ok = False
        consumer_data = None
        repeat = 20
        e_msg = None
        
        while not is_ok and repeat != 0:
            try: 
                consumer_data = KafkaConsumer(
                    value_deserializer=lambda data: json.loads(data.decode('utf-8')),
                    bootstrap_servers=self.servers
                )
                consumer_data.subscribe(topics=[self.topic_wine])
                is_ok = True
            except Exception as e:
                e_msg = e
                time.sleep(2)
                repeat -= 1
                
        if repeat == 0:
            raise RuntimeError(f"Cannot connect to Kakfa broker: {e_msg}")
        
        self.consumer_data = consumer_data
        self.postgres_db = manager.ManagerPostgres()
        
    def start(self):
        for message in self.consumer_data:
            data = message.value
            if message.topic == self.topic_wine and data["y"] is not None:
                self.postgres_db.add_new_prediction(data["X"], round(data["y"]))
