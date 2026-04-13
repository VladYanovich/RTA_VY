# Napisz konsumenta wykrywającego anomalie prędkości: alert jeśli ten sam user_id wykona więcej niż 3 transakcje w ciągu 60 sekund.

from kafka import KafkaConsumer
import json
from collections import defaultdict, deque
from datetime import datetime, timedelta

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='broker:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

user_transactions = defaultdict(deque)

Interval = 60
MAX_TX = 3

for message in consumer:
    tx = message.value
    
    user_id = tx['user_id']
    timestamp = datetime.fromisoformat(tx['timestamp'])
    
    user_queue = user_transactions[user_id]

    user_queue.append(timestamp)
    
    while user_queue and (timestamp - user_queue[0]).total_seconds() > Interval:
        user_queue.popleft()

    if len(user_queue) > MAX_TX:
        print(f"ALERT: {user_id} wykonał {len(user_queue)} transakcji w {Interval}s!")


