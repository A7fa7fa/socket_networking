from msg import create_msg
from sock.sock import MySocket, ADDR
import threading


def test_client_run() -> None:
    """create connection and sends msg to server"""

    client = MySocket()

    if not (client.connect(ADDR)):
        print(exit())

    client.send_msg(create_msg())
    server_msg = client.recieve_msg()

    client.send_msg(create_msg())
    client.send_msg(create_msg())
    client.send_msg(create_msg())
    client.send_msg(create_msg())
    client.sock.close()

    print(f"recived data {server_msg}")


if __name__ == '__main__':
    test_client_run()
