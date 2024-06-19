# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.connect(('localhost', 3030))
#
# s.sendall('Hello!!!'.encode('utf-8'))
#
# data = s.recv(1024)
# print('client: ' + data.decode('utf-8'))
# s.close()
##################
# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# hostname = socket.gethostname()
# port = 12345
#
# s.connect((hostname, port))
#
# filename = 'video2.MP4'
#
# print('receiving data from server')
#
# file = open(filename, 'wb')
#
# while 1:
#     data = s.recv(4096)
#     file.write(data)
#     if not data:
#         break
#
# s.close()
# print('file downloaded')

############################

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hostname = socket.gethostbyname(socket.gethostname())
port = 9090

server = hostname, port

def read_sock():
    while 1:
        data = s.recv(1024)
        print(data.decode('utf-8'))

alias = input('Enter you name: ')
s.bind(('', 0))
s.sendto((alias + ' connect to server').encode('utf-8'), server)

thr = threading.Thread(target=read_sock)
thr.start()

while 1:
    msg = input()
    s.sendto(('['+alias+'] ' + msg).encode('utf-8'), server)
