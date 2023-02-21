from uuid import uuid4


def create_msg() -> dict:

    rand = str(uuid4())
    msg = {"body": {"msg": "This is a test.", "random": rand}}
    return msg
