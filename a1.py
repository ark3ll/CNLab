import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_port = ("143.47.184.219", 5378)
client.connect(host_port)

while True:
    name = input("Please select a username: ")
    string_bytes = ("HELLO-FROM " + name + "\n").encode("utf-8")
    bytes_length = len(string_bytes)
    num_bytes = bytes_length
    while num_bytes > 0:
        num_bytes -= client.send(string_bytes[bytes_length - num_bytes :])

    response = ""
    while True:
        data = client.recv(1)
        data = data.decode()
        if data == "\n":
            break
        response += data

    if response == "IN-USE":
        print("This name is in use")
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(host_port)

    elif response == "BUSY":
        print("Maximum number of clients has been reached, Try again later")
        client.close()

    else:
        print(response)
        break


def other(client):
    while True:
        message = ""
        while True:
            try:
                data = client.recv(1).decode()
                if data == "\n":
                    break
                message += data
            except OSError as msg:
                break
        if message == "BAD-DEST-USER":
            print("User not recognised, try again.")

        elif message == "BAD-RQST-HDR":
            print("An error occurred, please try again.")

        elif message == "BAD-RQST-BODY":
            print("An error occurred, please try again.")
        elif message == "SEND-OK":
            print("Message sent.")
            continue
        elif message.startswith("DELIVERY"):
            message = message.replace("DELIVERY", "\b")
            print(message)
        else:
            print(message)


t = threading.Thread(daemon=True, target=other, args=(client,))
t.start()

while True:
    msg = input("")

    try:
        if msg.startswith("@"):
            recipient, msg = msg.split(maxsplit=1)
            string_bytes = ("SEND " + recipient[1:] + " " + msg + "\n").encode("utf-8")
            bytes_length = len(string_bytes)
            num_bytes = bytes_length
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_length - num_bytes :])

        elif msg == "!who":
            string_bytes = ("LIST\n").encode("utf-8")
            bytes_length = len(string_bytes)
            num_bytes = bytes_length
            while num_bytes > 0:
                num_bytes -= client.send(string_bytes[bytes_length - num_bytes :])

        elif msg == "!quit":
            kill_listener = True
            client.close()
            print("The chat room has been closed")
            break

        else:
            print("Given command is invalid")

    except KeyboardInterrupt:
        client.close()
        break
