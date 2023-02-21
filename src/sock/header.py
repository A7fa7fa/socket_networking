def len_inbytes(msg: str, length: int) -> bytes:
    """returns length of bytearray `bmsg` as byte"""
    return len(msg).to_bytes(length, byteorder='big')


def len_frombytes(bmsg: bytearray) -> int:
    """returns length of bytearray `bmsg` as integer"""
    try:
        return int.from_bytes(bmsg, byteorder='big')
    except Exception as e:
        print(e)
        return None
