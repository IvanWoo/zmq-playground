import threading
import zmq
import time
from random import randint

context = zmq.Context()


def subscriber1():
    counter = 0
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt(zmq.SUBSCRIBE, b"news")
    while True:
        message = socket.recv_multipart()
        print(f"[{counter}] Subscriber 1 received: {message}")
        time.sleep(randint(0, 3))
        counter += 1


def subscriber2():
    counter = 0
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://localhost:5555")
    socket.setsockopt(zmq.SUBSCRIBE, b"news")
    while True:
        message = socket.recv_multipart()
        print(f"[{counter}] Subscriber 2 received: {message}")
        time.sleep(randint(0, 3))
        counter += 1


thread1 = threading.Thread(target=subscriber1)
thread2 = threading.Thread(target=subscriber2)
thread1.start()
thread2.start()
