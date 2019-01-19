import socket
def client_sock(curr_url):
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect(('blujay.dyn.wpi.edu', 9995))
    my_sock.sendall(b'POST / HTTP/1.1 HOST: ' + curr_url.encode())
    response = my_sock.recv(1024)
    my_sock.close()
    return(response)

print(client_sock('https://www.youtube.com/watch?v=hwMkMoSMK6o'))
