import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
counter = 0

while True:
    topic = b"news"
    message = b"Breaking news: The sky is blue."
    socket.send_multipart([topic, message])
    print(f"[{counter}] Publisher sent {[topic, message]}")
    time.sleep(1)
    counter += 1
