import random
import socket
import time
import video_process
import json
import pickle
import os

save_dir = 'processed_vids'
if os.path.exists(save_dir):
    with open(save_dir, 'rb') as f:
        processed_vids = pickle.load(f)

else:
    processed_vids = {}


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
            str_data = str_data[starting_index:]
            print(str_data)
            if str_data in list(processed_vids.keys()):
                response_val = processed_vids[str_data]
            else:
                response_val = video_process.process_video_url(str_data)
                if response_val:
                    processed_vids[str_data] = response_val
                    with open(save_dir, 'wb') as w:
                        pickle.dump(processed_vids, w, protocol=pickle.HIGHEST_PROTOCOL)
            c.sendall(str(response_val).encode())
        c.close()

make_server()
