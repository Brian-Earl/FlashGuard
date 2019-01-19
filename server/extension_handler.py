import random
import socket
import time

s = socket.socket()       
host = socket.getfqdn()
port = 9992
buffSize = 1024
s.bind((host, port))

print ('Starting server on', host, port)

s.listen(5)

print ('Entering infinite loop; hit CTRL-C to exit')
while True:
    c, (client_host, client_port) = s.accept()
    print ('Got connection from', client_host, client_port)
    data = c.recv(buffSize)
    print(data)
    c.sendall(b'HTTP/1.0 200 OK\n')
    c.sendall(b'Content-Type: text/html\n')
    c.sendall(b'\n')
    c.sendall(b"""
        <html>
        <body>
        <h1>Hello World</h1> this is my server!
        </body>
        </html>
    """)
    c.close()
