import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1250))

uzenet = s.recv(1024)
print(uzenet.decode('utf-8'))