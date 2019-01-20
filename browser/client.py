import socket
import json

with open('config.json') as f:
    data = json.load(f)


def client_sock(curr_url):
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect((data['server_host'], data['server_port']))
    my_sock.sendall(b'POST / HTTP/1.1 HOST: ' + curr_url.encode())
    response = my_sock.recv(1024)
    my_sock.close()
    response = response.decode()
    if(response == "True"):
        return 1
    elif(response == "False"):
        return 0
    else:
        return -1

#print(client_sock('https://www.youtube.com/watch?v=hwMkMoSMK6o'))
