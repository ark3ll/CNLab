import socket

from _thread import *
import threading

server_ip = "143.47.184.219"
server_port = "5378"

s = socket.socket()

print(f"[*] Connecting to {server_ip}:{server_port}...")

s.connect((server_ip, int(server_port)))
print("[+] Connected.")

name = input("Enter your name: ")
