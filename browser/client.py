
import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('autoreg-119616.dyn.wpi.edu', 9997))
mySock.sendall(b'POST / HTTP/1.1 HOST: www.youtube.com/watch?v=XTbTykMlhOk')
response = mySock.recv(1024)
print(response)
mySock.close()
