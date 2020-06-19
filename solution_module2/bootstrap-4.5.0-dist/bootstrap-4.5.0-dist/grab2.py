import socket
s = socket.socket()
s.connect(("192.168.183.3", 22))
print s.recv(1024)
s.close()
