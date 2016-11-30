import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 4234))
s.listen(1)
while True:
    client, addr = s.accept()
    while True:
 kugfout