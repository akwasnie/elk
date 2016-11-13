import socket

ip = '127.0.0.1'
port = 5000
buffer_size = 1024
msg = ''

while True:
    msg = raw_input('msg: ')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.send(msg)
    s.close()
