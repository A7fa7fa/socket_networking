import threading
from typing import NoReturn
from msg import create_msg
from sock.sock import MySocket, ADDR


def handle_client(conn: MySocket, addr: tuple) -> None:
    """handels new connection in separate thread"""

    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        # TODO Handshake (HTTP Upgrade)
        client_msg = conn.recieve_msg()

        if not client_msg:
            print('no message')
            break

        print(f"recived data {client_msg}")

        # do stuff here

        conn.send_msg(create_msg())
    conn.sock.close()
    print(f'[CLIENT DISCONNECTED] {addr}')


def startServer() -> NoReturn:

    # create a costume socket of MySocket Class
    server = MySocket()

    # bind it to the public interface
    server.sock.bind(ADDR)

    MAX_CONNECTIONS = 5
    server.sock.listen(MAX_CONNECTIONS)

    print(f'[SERVER] is listening on {ADDR}')

    while True:
        conn, addr = server.sock.accept()
        conn = MySocket(sock=conn)

        # start separate thread to handle new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr,))
        thread.start()

        print(f"ACTIVE CONNECTIONS {threading.active_count() -1}")


if __name__ == '__main__':
    startServer()
