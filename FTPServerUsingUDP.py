
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  FTPServerUsingUDP                                     
                                                             

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Including Header files for predifined methods and data types
from socket import *
import os
import re
import hashlib
from os.path import join

# Transferring the contents of the file requested by the client
# The file is opened in binary mode
def begin_file_transfer(file_name):
    file_read = open(file_name,'rb')
    data_Source = file_read.read(1024)
    while (data_Source):
        connection_server_socket_udp.sendto(data_Source,clientAddress)
        data_Source = file_read.read(1024)
    file_read.close()
    connection_server_socket_udp.sendto("EOF".encode(),clientAddress)
    print("File Transmission completed using UDP")
    print("")
    print("EOF: End of File Transfer")
    print

# Calculating the checksum of the requested file
def check_checksum(file_name):
    file_read = open(file_name,'r')
    accrue = 0
    line = file_read.readline()
    while line:
        for data in line:
            accrue += ord(data)
        line = file_read.readline()
    file_read.close()
    return accrue

#   Set up the port number  
#   Waiting to the requests from the client
server_port_number_udp = 13080
server_port_number_tcp = 9100

#Bind port number for connecting to the server
connection_server_socket = socket(AF_INET,SOCK_STREAM)
connection_server_socket.bind(("",server_port_number_tcp))

#server start listening for incoming request
connection_server_socket.listen(1)

#Bind port number for connecting to the server
connection_server_socket_udp = socket(AF_INET, SOCK_DGRAM)
connection_server_socket_udp.bind(("", server_port_number_udp))

#Server starts listening to requests from clients
print("The server is ready to receive the request from the clients :- ")
print("")
while 1:
    #server waits for incoming requests
    file_name_input, clientAddress = connection_server_socket_udp.recvfrom(1024)
    connection_client_socket, addr = connection_server_socket.accept()

    # Read the name of the file sent from the client
    file_name = file_name_input.decode()
    print("File Name: ",file_name)
    print("")
    filePath="INIT"
    search_result = 0

    #chekcing the file whether it is present in the mentioned path
    for root, dirs, files in os.walk('E:\\'):
        
        if file_name in files:
            search_result = 1
            filePath=join(root, file_name)
            print("File Found at : %s" % join(root, file_name))
            print("")
            break

    #   The file has been found on the server
    #   send notification to client stating that the file transfer begins

    if  search_result == 1:
        connection_server_socket_udp.sendto("FILE FOUND IN THE SERVER".encode(), clientAddress)
        checksum = check_checksum(filePath)
        print("The checksum of the requested file is ",checksum)
        print("")
        connection_client_socket.send(str(checksum).encode())
        begin_file_transfer(filePath)
        connection_server_socket_udp.close()
        break


    #   The file requested by the client is not found on the server
    else:
        print("File not found in the server")
        print("")
        connection_server_socket_udp.sendto("FILE NOT FOUND IN THE SERVER".encode(),clientAddress)
        connection_server_socket_udp.close()
        break
        
