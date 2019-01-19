import random
import socket
import time
import server.video_process
import browser.browser

def make_server():
    s = socket.socket()
    host = socket.getfqdn()
    port = 9997
    buffSize = 1024
    s.bind((host, port))
    print('Starting server on', host, port)
    s.listen(5)
    print ('Entering infinite loop; hit CTRL-C to exit')
    while True:
        c, (client_host, client_port) = s.accept()
        print ('Got connection from', client_host, client_port)
        data = c.recv(buffSize)
        if(b'youtube.com/watch' in data):
            if(video_process.process_video_url(data[22:])):
                browser.pause_vid()
        c.sendall(b'HTTP/1.1 200 OK')
        c.sendall(b'Content-Type: text/html')
        c.sendall(b"""
            <html>
            <body>
            <h1>this is my server!</h1>
            </body>
            </html>
        """)
        c.close()
