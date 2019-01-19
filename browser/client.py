import socket
def client_sock(curr_url):
    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
    my_sock.connect(('', 9995))
=======
    my_sock.connect(('blujay.dyn.wpi.edu', 9995))
>>>>>>> ee5bd5f0c2e9cc99eaf6f71e9544cddbed86044e
    my_sock.sendall(b'POST / HTTP/1.1 HOST: ' + curr_url.encode())
    response = my_sock.recv(1024)
    my_sock.close()
    return(response)

print(client_sock('https://www.youtube.com/watch?v=hwMkMoSMK6o'))
