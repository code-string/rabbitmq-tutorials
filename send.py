import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')) # establish connection with RabbitMQ server on localhost

channel = connection.channel()

# create a queue called 'hello' which message will be delivered
channel.queue_declare(queue='hello')

# send message to queue via default exchange (identified by '')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# close connection
connection.close()

