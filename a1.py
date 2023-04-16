import socket
import threading

username = input("Choose a username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#defines and connects to port
host_port = ("143.47.184.219", 5378)
client.connect(host_port)

# def receive():
#     while True:
#         try:
#             bytes_len = len(string_bytes)
#             num_bytes = bytes_len
#             while num_bytes > 0:
#             num_bytes -= client.send(string_bytes[bytes_len-num_bytes:]) 
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



while True:
    name = input("Enter Username: ")
    string_bytes = ("HELLO-FORM" + name + "\n").encode("utf-8")
    bytes_len = len(string_bytes)
    num_bytes = bytes_len
    while num_bytes > 0:
        num_bytes -= client.send(string_bytes[bytes_len-num_bytes:]) 

    data = client.recv(4096).decode()
    print(data)

    if data == "IN-USE\n":
        client.close()
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(server_port)

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




        

    

# client.connect((server_ip, int(server_port)))
# print("[+] Connected.")

