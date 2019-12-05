import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('0.0.0.0',2222))
s.listen(5)
while True:
    conn,addr = s.accept()
    while True:
        data = s.recv(1024)
        if data == 'close':
            break
        s.send(data)
    s.close()