
def encode_msg(format: str, msg: str) -> bytes:
    """convert the str `msg` to bytes"""

    return msg.encode(encoding=format, errors='strict')


def decode_msg(format: str, msg: bytearray) -> str:
    """convert the bytes `msg` to str"""

    return msg.decode(encoding=format, errors='strict')
