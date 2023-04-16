import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#defines and connects to port
host_port = ("143.47.184.219", 5378)
client.connect(host_port)

while True:
    name = input("Enter Username: ")
    string_bytes = ("HELLO-FROM" + name + "\n").encode("utf-8")
    bytes_len = len(string_bytes)
    num_bytes = bytes_len
    while num_bytes > 0:
        num_bytes -= client.send(string_bytes[bytes_len-num_bytes:]) 

    data = client.recv(4096).decode()
    print(data)

    if data == "IN-USE\n":
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(host_port)

    elif data == "BUSY/n":
        print("Maximum number of clients has been reached, Try again later")
        client.close
    else:
        break

def other(client):
    while True:
        try:
            print(client.recv(4096).decode())
        
        except OSError as msg:
            print(msg)

t = threading.Thread(daemon=True, target=other, args=(client,))
t.start()

while True:

    message = input("")

    try:
        if message == "!who":
            string_bytes  = ("LIST\n").encode("utf-8")
            bytes_len = len(string_bytes)
            num_bytes = bytes_len
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_len - num_bytes:])

        elif message.startswith("@"):
            to_user, msg = message.split(maxsplit=1)
            string_bytes = ("SEND " + to_user[1:] + " " + msg + "\n").encode("utf-8")
            bytes_len = len(string_bytes)
            num_bytes = bytes_len
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_len - num_bytes:])
        
        elif message == "!quit":
            client.close()
            print("Client is closed")
            break
        
        else:
            print("Invalid command")

    except(KeyboardInterrupt):
        client.close()