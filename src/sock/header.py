def int_to_bytes(num: int, length: int) -> bytes:
    """returns length of `msg` as byte array of size `length`"""
    return int(num).to_bytes(length, byteorder='big')


def bytes_to_int(msg: bytearray) -> int:
    """converts bytearray `msg` to integer"""
    try:
        return int.from_bytes(msg, byteorder='big')
    except Exception as e:
        print(e)
        return None
