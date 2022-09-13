# let's write the code!

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# now i have made my socket
mysock.connect(('127.0.0.1', 9000))
# connect it to
cmder = 'GET http://127.0.0.1/remeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmder)


while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = ' ')


mysock.close()


