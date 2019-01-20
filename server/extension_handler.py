import random
import socket
import time
import video_process
import json



def make_server():
    with open('../config.json') as f:
        data = json.load(f)

    s = socket.socket()
    host = socket.gethostbyname(data['server_host'])
    port = data['server_port']
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
            str_data = data.decode()
            starting_index = str_data.index('http')
            print(data[starting_index:])
            response_val = video_process.process_video_url(str_data[starting_index:])
            c.sendall(str(response_val).encode())
        c.close()

make_server()
