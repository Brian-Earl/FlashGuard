import socket
def client_sock(curr_url):
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_sock.connect(('autoreg-119616.dyn.wpi.edu', 9997))
    my_sock.sendall(b'POST / HTTP/1.1 HOST: ' + curr_url)
    response = my_sock.recv(1024)
    my_sock.close()

client_sock(b'https://www.youtube.com/watch')
