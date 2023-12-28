import pika, sys, os, time,requests
from bs4 import BeautifulSoup


def image_counter(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'}
    result = requests.get(url, headers=headers)

    soup = BeautifulSoup(result.text, 'html.parser')
    images_in_bs4 = soup.find_all("img")
    image_list = [image for image in images_in_bs4]
    return len(image_list)

def main():
    connection_parameters = pika.ConnectionParameters(host='localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue='hello', durable=True)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        img_len = image_counter(body.decode())
        print(f"[x] Done. There is {img_len} images in this url")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='hello',
        on_message_callback=callback,
    )

    print(" [*] Waiting for messages. To exit press CTRL")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
