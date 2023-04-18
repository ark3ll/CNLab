import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# defines and connects to port
host_port = ("143.47.184.219", 5378)
client.connect(host_port)

while True:
    name = input("Please select a username: ")
    string_bytes = ("HELLO-FROM " + name + "\n").encode("utf-8")
    bytes_length = len(string_bytes)
    num_bytes = bytes_length
    while num_bytes > 0:
        num_bytes -= client.send(string_bytes[bytes_length - num_bytes :])
        data = client.recv(1).decode()
        print(data)



    # data = client.recv(0).decode()
    # while True:
    #     chunk = client.recv(1).decode()
    #     if not chunk:
    #         break
    #     data += chunk
    
    # data = client.recv(4096).decode()
    

    # print(data)

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
    msg = input("")

    try:
        if msg == "!who":
            string_bytes = ("LIST\n").encode("utf-8")
            bytes_length = len(string_bytes)
            num_bytes = bytes_length
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_length - num_bytes :])

        elif msg.startswith("@"):
            recipient, msg = msg.split(maxsplit=1)
            string_bytes = ("SEND " + recipient[1:] + " " + msg + "\n").encode("utf-8")
            bytes_length = len(string_bytes)
            num_bytes = bytes_length
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_length - num_bytes :])

        elif msg == "!quit":
            client.close()
            print("The chat room has been closed")
            break

        else:
            print("Given command is invalid")

    except KeyboardInterrupt:
        client.close()
        break
