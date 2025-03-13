#!/usr/bin/env python3
import socket

target_host = "www.google.com"
target_port = 80

# initialize a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET specifies that we are using IPV4
# SOCK_STREAM specifies that we want to use a TCP client

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()
