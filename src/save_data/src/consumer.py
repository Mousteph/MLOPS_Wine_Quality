from kafka import KafkaConsumer
import json
from typing import List
from postgresql import manager

class ConsumerManager:
    def __init__(self, servers: List, topic_success: str, topic_error: str):
        self.servers = servers
        self.topic_success = topic_success
        self.topic_error = topic_error
        
        self.consumer_data = KafkaConsumer(
            value_deserializer=lambda data: json.loads(data.decode('utf-8')),
            bootstrap_servers=self.servers
        )
        self.consumer_data.subscribe(topics=[self.topic_success, self.topic_error])

        
        self.postgres_db = manager.ManagerPostgres()
        
    def start(self):
        for message in self.consumer_data:
            data = message.value
            if message.topic == self.topic_success:
                self.postgres_db.add_new_prediction(data["X"], data["y"])
