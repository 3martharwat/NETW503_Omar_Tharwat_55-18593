import socket
import select
import sys
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port=5618
server_socket.bind(('172.20.10.3',port))
server_socket.listen(5)
while True :
 client_socket, client_address = server_socket.accept()
 while True: 
  msg = client_socket.recv(1024)
  if( not msg):
    break  
  message = msg.decode('utf-8')
  if message != "CLOSE SOCKET":
    message=message.upper()
    msg=message.encode('utf-8')
    client_socket.send(msg)
  else :
    client_socket.close()
    break

  
  


