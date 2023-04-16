# import socket
# import threading

# username = input("Choose a username: ")
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #defines and connects to port
# host_port = ("143.47.184.219", 5378)
# client.connect(host_port)

# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('ascii')
#             if message == 'NICK':
#                 client.send(username.encode('ascii'))
#             else:
#                 print(message)
#         except:
#             print("An error occurred!")
#             client.close()
#             break
# def write():
#         while True:
#             message = f'{username}: {input("")}'
#             client.send(message.encode('ascii'))

# receive_thread = threading.Thread(target=receive)
# receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start()



# while True:
#     name = input("Enter Username: ")
#     string_bytes = ("HELLO-FORM" + name + "\n").encode("utf-8")
#     bytes_len = len(string_bytes)
#     num_bytes = bytes_len
#     while num_bytes > 0:
#         num_bytes -= s.send(string_bytes[bytes_len-num_bytes:]) 

#     data = s.recv(4096).decode()
#     print(data)

#     if data == "IN-USE\n":
#         s.close()
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect(server_port)

#     elif data == "BUSY/n":
#         print("Maximum number of clients has been reached, Try again later")
#         s.close
#     else:
#         break
# s.connect((server_ip, int(server_port)))
# print("[+] Connected.")

while True:

message = input("")

try:
    if message == "!who":
        string_bytes  = ("LIST\n").encode(utf-8)
        bytes_len = len(string_bytes)
        num_bytes_to_send = bytes_len
        while num_bytes_to_send > 0:
            num_bytes_to_send -= client.send(string_bytes[bytes_len - num_bytes_to_send:])

    elif message.startswith("@"):
        to_user, msg = message.split(maxsplit=1)
        string_bytes = ("SEND " + to_user[1:] + " " + msg + "\n").encode("utf-8")
        bytes_len = len(string_bytes)
        num_bytes_to_send = bytes_len
        while num_bytes_to_send > 0:
            num_bytes_to_send -= client.sec(string_bytes[bytes_len - num_bytes_to_send:])
    
    elif message == "!quit":
        client.close()
        print("Client is closed")
        break
    
    else:
        print("Invalid command")
