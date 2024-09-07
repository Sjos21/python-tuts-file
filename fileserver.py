import socket
host='localhost'
port=6767
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("Server is listening on:",port)
s.listen()
c,addr= s.accept()

fileName = c.recv(1024)
try:
    f=open(fileName,"rb")
    content=f.read()
    c.send(content)
    f.close()
except fileNotFoundError:
    c.send(b"File does not exist")

c.close()