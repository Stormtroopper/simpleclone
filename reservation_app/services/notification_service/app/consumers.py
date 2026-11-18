import asyncio
import json
from aiokafka import AIOKafkaConsumer
from datetime import datetime
#KAFKA configuration 
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = [
    "reservation.cancelled",
    "reservation.made",
    "user.registered",
    "user.logged_in",
    "user.logged_out",
    "password.changed"
]
async def handle_event(topic: str, data: dict):
    """
    Process incoming events.
    """
    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Received event from topic: {topic}")
    print(json.dumps(data, indent=2, default=str))

    if topic == "reservation.created":
        # Example: send confirmation notification
        user_id = data.get("user_id")
        print(f"Sending booking confirmation to user {user_id}")

    elif topic == "reservation.cancelled":
        user_id = data.get("user_id")
        print(f"Sending cancellation notice to user {user_id}")

    elif topic == "user.created":
        print(f"Sending welcome email to {data.get('email')}")
async def start_consumers():
    consumer=AIOKafkaConsumer(
        *KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id="notification-service-group",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")), )
    await consumer.start()
    print("Kafka consumer started and listening ......", KAFKA_TOPIC)
    try:
        async for message in consumer:
            await handle_event(message.value)
    except Exception as e:
        print(f"Error while consuming messages: {e}")
    finally:
        await consumer.stop()
        print("Kafka consumer stopped.")
async def run_consumer():
    while True:
        try:
            await start_consumers()
        except Exception as e:
            print(f"Error in consumer loop: {e}")
            await asyncio.sleep(5)  # Wait before retrying