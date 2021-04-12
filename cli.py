#client code
import socket

c.connect(('localhost',9999))
name=input('enter your name')
c.send(bytes(name,'utf=8'))

print(c.recv(1024))
c=socket.socket()

c.connect(('localhost',9999))
name=input('enter your name')
c.send(bytes(name,'utf=8'))

print(c.recv(1024))

#server code

import socket

s=socket.socket()
print("socket created")

s.bind(('localhost',9999))

s.listen(3)
print("waiting for connection")

while True:
    c,addr=s.accept()
    name=c.recv(1024).decode()
    print("connection with",addr,name)
    c.send(bytes("welcome to suriya",'utf-8'))
    c.close()


