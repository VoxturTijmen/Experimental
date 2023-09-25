import pika

def main():
    options = {
        "A": {
            "desc": "Send message to A: ",
            "func": func_a
        },
        "B": {
            "desc": "Send message to B: ",
            "func": func_b
        }
    }

    while True:
        choose(options)


def choose(options: dict):
    keys = [key for key in options.keys()]

    choice = input(f"Choose: {', '.join(keys)}: ").upper()

    try: 
        options[choice]
    except:
        print("No.")
        return

    message = input(options[choice]['desc'])

    options[choice]['func'](message)


def func_a(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='queue_a')

    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")
    connection.close()


def func_b(message: str):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='queue_b')

    channel.basic_publish(exchange='', routing_key='hello', body=message)
    print(f" [x] Sent '{message}'")
    connection.close()


if __name__ == "__main__":
    main()
