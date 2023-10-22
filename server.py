import socket
import threading
PORT = 1501
ADDR = ('127.0.0.1', PORT)
def threaded(conn, addr):
 print("[NEW CONNECTION] " + str(addr) + " connected." + "\n" )
 while True :
 # Functionality of the server
 #
 #
 # do not forget to release the thread if you've locked it
  message =  conn.recv(1024).decode('utf-8')
  if message != "CLOSE SOCKET":
    message=message.upper()
    msg=message.encode('utf-8')
    conn.send(msg)
  else :
    print( str(addr) + " is disconnected.")
    conn.close()
    break



def main():
  print(" Server is starting...")
  # Open server socket as in MS0
  #
  #
  server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server_socket.bind(ADDR)
  server_socket.listen(5)
  while True:
    client_socket, client_address = server_socket.accept()
    # Locking the thread that will be assigned to the client
    threading.Lock().acquire()
    # start new thread
    #
    #
    thread = threading.Thread(target=threaded,args=(client_socket, client_address))
    thread.start()

  
    print("[ACTIVE CONNECTIONS]" + str(threading.active_count() - 5) + "\n")
if __name__ == "__main__":
 main()

  
  


