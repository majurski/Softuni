import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (PORT, SERVER)

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM)
server.bind(ADDR)
