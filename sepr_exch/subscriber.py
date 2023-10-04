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
    x = list(range(1, 4))
    x.reverse()
    for i in x:
        print(f" [*] Processing... [{i}] second{'' if i == 1 else 's'} left.")
        time.sleep(1)
    print("Ready!")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
