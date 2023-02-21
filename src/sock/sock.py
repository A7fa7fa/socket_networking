import socket
import json
# from sock.address import __initserverhost
from sock.converter import decode_msg, encode_msg
from sock.header import len_frombytes, len_inbytes


# the first `BYTE_COUNT` of msg recieved or send are the length of msg
BYTE_COUNT = 4

# local IPV4 Adress
SERVER = socket.gethostbyname(socket.gethostname())
# external IPV4 Adress
# SERVER = __initserverhost()

PORT = 5051

# on this addr socket will listen create connections from
ADDR = (SERVER, PORT)

# decrypt/encrypt msg in this format
FORMAT = 'UTF-8'


class MySocket:
    """simple socket wrapper"""

    def __init__(self, sock=None) -> None:
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        else:
            self.sock = sock

    def connect(self, addr) -> bool:
        try:
            self.sock.connect(addr)
            return True
        except Exception as e:
            print(e)
            return False

    def send_msg(self, msg: dict) -> None:
        """Send a json message via the socket."""

        encoded_msg = encode_msg(FORMAT, json.dumps(msg))
        header = len_inbytes(encoded_msg, BYTE_COUNT)
        msg = self.__add_msg_header(header, encoded_msg)

        self.sock.sendall(msg)

    def recieve_msg(self) -> str:
        """Receive a message via the socket."""

        raw_msg_len = self.__read_header()

        if not raw_msg_len:
            return None

        msg_body_len = len_frombytes(raw_msg_len)
        if not msg_body_len:
            return None
        raw_msg = self.__recieve_certain_msg_len(msg_body_len)
        return decode_msg(FORMAT, raw_msg)

    def __read_header(self) -> bytearray:
        """The header tells the message size in bytes. Header is of length `BYTE_COUNT`)"""
        return self.__recieve_certain_msg_len(BYTE_COUNT)

    def __recieve_certain_msg_len(self, length) -> bytearray:
        """Get a message of a certain length from the socket stream"""

        data = bytearray()
        while len(data) < int(length):  # check if still connected or in try/expet
            try:
                packet = self.sock.recv(int(length) - len(data))
                if not packet:
                    return None
                data.extend(packet)
            except Exception as e:
                print(e)
                return None

        return data

    def __add_msg_header(self, header: bytes, msg: bytes) -> bytes:
        """combines header and msg """

        return header + msg
