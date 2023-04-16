import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#defines and connects to port
server_port = ("143.47.184.219", 5378)
s.connect(server_port)

while True:
    name = input("Enter Username: ")
    string_bytes = ("HELLO-FORM" + name + "\n").encode("utf-8")
    bytes_len = len(string_bytes)
    num_bytes = bytes_len
    while num_bytes > 0:
        num_bytes -= s.send(string_bytes[bytes_len-num_bytes:]) 

    data = s.recv(4096).decode()
    print(data)

    if data == "IN-USE\n":
        s.close()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(server_port)

    elif data == "BUSY/n":
        print("Maximum number of clients has been reached, Try again later")
        s.close
    else:
        break




        

    

s.connect((server_ip, int(server_port)))
print("[+] Connected.")

