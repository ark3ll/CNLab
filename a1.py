import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#defines and connects to port
host_port = ("143.47.184.219", 5378)
client.connect(host_port)

while True:
    name = input("Enter Username: ")
    string_bytes = ("HELLO-FROM " + name + "\n").encode("utf-8")
    bytes_length = len(string_bytes)
    num_bytes = bytes_length
    while num_bytes > 0:
        num_bytes -= client.send(string_bytes[bytes_length-num_bytes:]) 

    data = client.recv(4096).decode()
    print(data)

    if data == "IN-USE\n":
        print("This username has been taken, please choose another one")
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(host_port)

    elif data == "BUSY/n":
        print("The chat room has reach maximum occupancy, please try again later")
        client.close
    else:
        break

def other(client):
    while True:
        try:
            print(client.recv(4096).decode())
            msg = input()

        except OSError as msg:
            print(msg)
        
t = threading.Thread(daemon=True, target=other, args=(client,))
t.start()

while True:

    msg = input("")

    try:
        if msg == "!who":
            string_bytes  = ("LIST\n").encode("utf-8")
            bytes_length = len(string_bytes)
            num_bytes = bytes_length
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_length - num_bytes:])

        elif msg.startswith("@"):
            to_user, msg = msg.split(maxsplit=1)
            string_bytes = ("SEND " + to_user[1:] + " " + msg + "\n").encode("utf-8")
            bytes_length = len(string_bytes)
            num_bytes = bytes_length
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_length - num_bytes:])
        
        elif msg == "!quit":
            client.close()
            print("Client is closed")
            break
        
        else:
            print("Invalid command")

    except KeyboardInterrupt:
        client.close()
        break
        