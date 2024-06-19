# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.SOCK_DGRAM
#
# s.bind(('localhost', 3030))
# s.listen(1)
#
# conn, addr = s.accept()
#
# while 1:
#     data = conn.recv(1024)
#     if not data:
#         break
#     conn.sendall(data)
#     print('server: ' + data.decode('utf-8'))
# conn.close()
##################

# import socket
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.SOCK_DGRAM
# hostname = socket.gethostname()
# port = 12345
#
# server.bind((hostname, port))
# server.listen(5)
#
# conn, addr = server.accept()
#
# filename = 'video.MP4'
#
# file = open(filename, 'rb')
# print('sending data to client')
#
# while 1:
#     file_data = file.read(4096)
#     conn.send(file_data)
#     if not file_data:
#         break
#
# file.close()
# conn.close()
# server.close()
# print('file sended')

#############

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # socket.SOCK_DGRAM
hostname = socket.gethostbyname(socket.gethostname())
port = 9090

server.bind((hostname, port))
# server.listen(5)

clients = []

print('start server')

while 1:
    data, address = server.recvfrom(1024)
    print(address[0], address[1])
    if address not in clients:
        clients.append(address)

    for cl in clients:
        if cl == address:
            continue
        server.sendto(data, cl)



