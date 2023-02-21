from requests import get


def __initserverhost() -> str:
    ip = get('https://api.ipify.org').text
    return ip
