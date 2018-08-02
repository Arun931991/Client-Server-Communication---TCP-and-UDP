
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  FTPServerUsingTCP                                     
                                                             

  Module Description :
  
  This module will establish a TCP connection between the client and the server.
  Once the connection has been established the client will input the file-name
  it wants to read and gain access to that file over the TCP connection. If the
  file is found on the server side, message will be displayed accordingly.
  The TCP connection is reliable so the data transfer will take place without any
  data loss.


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Including Header files for predifined methods and data types
from socket import *
import os
import re
from os.path import join


# Assign a port number on which the server will be listening to the requests from the client
server_port_number = 9050

# Bind the port number for the server connection
connection_server_socket = socket(AF_INET,SOCK_STREAM)
connection_server_socket.bind(("",server_port_number))

# server starts waiting for incoming TCP requests
connection_server_socket.listen(1)

# Server starts listening to requests from clients
print ("The server is ready to receive the request from the clients :- ")
print("")

# Transfer the contents of the file requested by the client
# The file is opened in binary mode
def begin_file_transfer(file_name,connection_client_socket):
    file_read=open (file_name, "rb")
    data_Source = file_read.read(1024)
    while (data_Source):
        connection_client_socket.send(data_Source)
        data_Source = file_read.read(1024)
    file_read.close()
    print("File transmission completed")
    print("")
    print("EOF: End of File Transfer")
    print("")
    connection_client_socket.close()

while 1:
    
    # server waits for incoming requests
    connection_client_socket, addr = connection_server_socket.accept()         
    # Read the name of the file sent from the client
    file_name_client = connection_client_socket.recv(1024)
    file_name_decoded = file_name_client.decode('utf-8')
    file_name = file_name_decoded
    search_result = 0
    filePath="INIT"
    # Looking for the requested file in the path
    for root, dirs, files in os.walk('E:\\'):
        if file_name in files:
            search_result = 1
            filePath=join(root,file_name)
            print("File found at : %s" % join(root, file_name))
            print("")
            break

    #   The file has been found on the server
    #   send notification to client stating that the file transfer begins
    if search_result == 1:         
        bounded_file_name_client = "FILE FOUND IN THE SERVER".encode()
        connection_client_socket.send(bounded_file_name_client)
        begin_file_transfer(filePath,connection_client_socket)
    #   The file requested by the client is not found on the server
    else:        
        bounded_file_name_client = "FILE NOT FOUND IN THE SERVER".encode()
        connection_client_socket.send(bounded_file_name_client)        
        
        
# close the TCP connection
connection_client_socket.close()


