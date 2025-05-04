from confluent_kafka import Consumer, KafkaError
from .config import KafkaSSLConfig
import sys
import ssl

def create_ssl_consumer():
    conf = {
        "bootstrap.servers": KafkaSSLConfig.KAFKA_BROKER,
        "group.id": KafkaSSLConfig.GROUP_ID,
        'client.id': KafkaSSLConfig.KAFKA_CLIENT_ID,
        "auto.offset.reset": "earliest",
        "security.protocol": "ssl",
        "ssl.ca.location": KafkaSSLConfig.SSL_CAFILE,
        "ssl.certificate.location": KafkaSSLConfig.SSL_CERTFILE,
        "ssl.key.location": KafkaSSLConfig.SSL_KEYFILE,
    }
    return Consumer(conf)

def consume_messages():
    consumer = create_ssl_consumer()
    consumer.subscribe([KafkaSSLConfig.TOPIC])
    print(f"Kafka consumer is waiting for events")
    try:
        while True:
            msg = consumer.poll(1.0) # Timeout in seconds
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition {msg.partition()}")
                    continue
                else:
                    print(f"Consumer error: {msg.error()}", file=sys.stderr)
                    break
            print(f"Received: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages()