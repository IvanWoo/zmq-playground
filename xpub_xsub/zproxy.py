# https://gist.github.com/kianby/e1d455e5fb2a14f8dee3c02c337527f5
import zmq


def main():

    context = zmq.Context()

    # Socket facing producers
    frontend = context.socket(zmq.XPUB)
    frontend.bind("tcp://*:5559")

    # Socket facing consumers
    backend = context.socket(zmq.XSUB)
    backend.bind("tcp://*:5560")

    zmq.proxy(frontend, backend)

    # We never get here…
    frontend.close()
    backend.close()
    context.term()


if __name__ == "__main__":
    main()
