import socket
host='localhost'
port=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("Server is listening on:",port)
s.listen()
c,addr= s.accept()
print("Connection from: ",str(addr))

c.send(b"How are you")
c.send("bye".encode())
c.close()