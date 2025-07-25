from socket import socket, AF_INET, SOCK_STREAM


def get_service_ip_port():
    sock = socket(AF_INET, SOCK_STREAM)
    ip = "localhost"
    try:
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
    finally:
        sock.close()

    return ip
