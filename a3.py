import socket
import threading

port = 6969
host = "localhost"
address = (server, port)
format = "utf-8"
quit = "!quit"

server = socket.socket(socket.AF_INET, sock.sock_stream)
server.bind(address)

clients =set()
clients_lock = threading.Lock()

def handle_client(conn,address)
    pass

def start():
    socket.listen()
    while True:
        conn, address = server.accept()
        with clients_lock:
            client.add(conn)
        thread = threading.Thread(target=, args=(conn, address))
        thread.start()

start
