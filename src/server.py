from sock.sock import MySocket, ADDR
import threading

msg = {"type": "test_info", "body": {"msg": "This is a test."}}


def handle_client(conn, addr: tuple):
    """handels new connection in separate thread"""

    print(f"[NEW CONNECTION] {addr} connected." )

    while True:
        # TODO Handshake (HTTP Upgrade)
        client_msg = conn.recv_msg()

        if not client_msg: break

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


    # Enable a server to accept connections. 
    # If backlog is specified, it must be at least 0 (if it is lower, it is set to 0); 
    # it specifies the number of unaccepted connections that the system will allow before refusing new connections. 
    # If not specified, a default reasonable value is chosen.
    # The backlog parameter is now optional.
    server.sock.listen(5)
    print(f'[SERVER] is listening on {ADDR}')
    
    while True:
        conn, addr = server.sock.accept()
        conn = MySocket(sock=conn)

        # start separate thread to handle new connection
        thread = threading.Thread(target=handle_client, args=(conn, addr,))
        thread.start()
        
        print(f"ACTIVE CONNECTIONS {threading.active_count() -1}")


server()