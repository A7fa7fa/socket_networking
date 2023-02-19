from sock.sock import MySocket, ADDR
import threading

msg = {"type": "test_info", "body": {"msg": "This is a test."}}


def handle_client(conn, addr: tuple):
    """handels new connection in separate thread"""

    print(f"[NEW CONNECTION] {addr} connected." )

    while True:
        # TODO Handshake (HTTP Upgrade)
        client_msg = conn.recv_msg()

        if not client_msg: 
            print('no message')
            break

        print(f"recived data {client_msg}")

        # do stuff here

        conn.send_msg(msg)
    conn.sock.close()
    print(f'[CLIENT DISCONNECTED] {addr}')



def server():

    #create a costume socket of MySocket Class
    server = MySocket()

    #bind it to the public interface
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
    server()