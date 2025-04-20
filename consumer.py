from kafka import KafkaConsumer
consumer = KafkaConsumer('test-topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
for msg in consumer:
    print("Received:", msg.value.decode())
    break

