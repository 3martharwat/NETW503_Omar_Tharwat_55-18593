import socket
import select
import sys
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5618
client_socket.connect(('172.20.10.3',port)) 
while True:
 message=input("enter your message: ")
 if message!="CLOSE SOCKET":
    msg=message.encode('utf-8')
    client_socket.send(msg)
    msg=client_socket.recv(1024)
    message =msg.decode('utf-8')
    print(message)
 else:
  client_socket.close()

 

