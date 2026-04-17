import pika
import os
from consumer_interface import mqConsumerInterface
class mqConsumer(mqConsumerInterface):
    def __init__(self, exchange_name: str, binding_key: str, queue_name:str) -> None:
        # Save parameters to class variables
        self.exchange_name = exchange_name
        self.binding_key = binding_key
        self.queue_name = queue_name
        # Call setupRMQConnection
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)
        # Establish Channel
        channel = connection.channel()
        self.channel = channel
        self.connection = connection
        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange=self.exchange_name)

    def bindQueueToExchange(self, queueName: str, topic: str) -> None:
        # Bind Binding Key to Queue on the exchange
        self.channel.queue_bind(
            queue=queueName,
            routing_key=self.binding_key,
            exchange=self.exchange_name,
        )

    def createQueue(self, queueName: str) -> None:
        # Create Queue if not already present
        self.channel.queue_declare(queue=queue_name)
        # Set-up Callback function for receiving messages
        self.channel.basic_consume(
            queue_name, on_message_callback, auto_ack=False
        )

    def on_message_callback(self, channel, method_frame, header_frame, body):
        # De-Serialize JSON message object if Stock Object Sent
        message = json.loads(JsonMessageObject)
        # Acknowledge And Print Message
        self.channel.basic_ack(method_frame.delivery_tag, False)
        print(message)

    def startConsuming(self) -> None:
        # Start consuming messages
        self.channel.start_consuming()
