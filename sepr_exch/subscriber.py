import time
import pika


exch = input("Exchange to watch: ").lower()


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange=exch, exchange_type='fanout')

result = channel.queue_declare(queue=exch)
queue_name = result.method.queue

channel.queue_bind(exchange=exch, queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")
    # time.sleep(3)
    # print("3!")
    # time.sleep(3)
    # print("6!")
    # time.sleep(3)
    # print("9!")
    # time.sleep(3)
    print("Ready!")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
