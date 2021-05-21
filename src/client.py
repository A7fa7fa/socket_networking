from sock.sock import MySocket, ADDR
import threading
from uuid import uuid4


rand = str(uuid4())
msg = {"type": "test_info", "body": {"msg": "This is a test.", "random": rand}}


def test_client_run():
    """create connection and sends msg to server"""

    client = MySocket()

    if not(client.connect(ADDR)): print(exit())

    client.send_msg(msg)
    server_msg = client.recv_msg()

    client.sock.close()

    print(f"recived data {server_msg}")


test_client_run()

