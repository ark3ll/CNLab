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
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            message = conn.recv(1024).decode(format)
            if not message:
                break

            if message == quit:
                connected = False

            print(f"[{addr}] {message}")
            with clients_lock:
                for c in clients:
                    c.sendall(f"[{addr}] {message}".encode(format))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()

def start():
    print('[SERVER STARTED]')
    socket.listen()
    while True:
        conn, address = server.accept()
        with clients_lock:
            client.add(conn)
        thread = threading.Thread(target=, args=(conn, address))
        thread.start()

start

