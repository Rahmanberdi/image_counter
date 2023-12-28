import pika,sys

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)

messages = [
    'https://www.guru99.com/best-computer-networks-books.html',
    'https://www.timeout.com/film/best-movies-of-all-time',
    'https://www.officialcharts.com/charts/albums-chart/',
    'https://www.cbr.com/greatest-tv-shows-all-time/',
    'https://thegreatestbooks.org/lists/44',
    'https://www.babbel.com/en/magazine/the-10-most-spoken-languages-in-the-world'
]
for message in messages:
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message,
                          properties=pika.BasicProperties(
                              delivery_mode=pika.DeliveryMode.Persistent
                          ))
    print(f'Sent {message}')
