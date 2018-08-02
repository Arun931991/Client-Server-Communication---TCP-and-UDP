
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  MakeUpperCaseServerUsingTCP                                     
                                                             

  Module Description :
  
  This module will create a TCP connection between the client and the server.
  The client will then pass a string of lower case letters to the server over
  the connection.
  The server will take his as an input and with the help of a program it will convert
  the lower case letters to upper case letters.
  This string will then be passed back to the client over the same TCP connection
  and displayed it over the client interface.
  TCP is a reliable connection so the transfer occurs without the loss of data.
  
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# The socket module forms the basis of all the network communications in python.
# It enables the server to create sockets in the program.
from socket import *

# It assigns a port number on the server side which is used for the data transfer.
serverPort = 12015

# create TCP welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)
#The second parameter SOCK_STREAM denotes that it is a TCP connection
serverSocket.bind(("",serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(1)

# output to console that server is listening 
print ("The Make Upper Case Server running over TCP is ready to receive ... ")

while 1:
    # server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept()
     
    # read a sentence of bytes from socket sent by the client
    userInput = connectionSocket.recv(1024)

    # converting the bytes to string format
    decodedMessage=userInput.decode('utf-8')

    # output to console the sentence received from the client 
    print ("The character(s) sent from client to server : ", decodedMessage)
	 
    # convert the sentence to upper case
    capitalizedSentence = decodedMessage.upper()
	 
    # send back modified sentence over the TCP connection
    connectionSocket.send(bytes(capitalizedSentence,"UTF-8"))

    # output to console the sentence sent back to the client 
    print ("The character(s) which is sent back from server : ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()
