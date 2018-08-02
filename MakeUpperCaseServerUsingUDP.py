
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  MakeUpperCaseServerUsingUDP                                   
                                                             
  Module Description :
  
  This module will use the UDP connection to perform the data transfer.
  A UDP connection will be established between the client and the server.
  The client will then pass a string of lower case letters to the server over
  the connection.
  The server will take his as an input and with the help of a program it will convert
  the lower case letters to upper case letters.
  This string will then be passed back to the client over the same TCP connection
  and displayed it over the client interface.

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# The socket module forms the basis of all the network communications in python.
# It enables the server to create sockets in the program.
from socket import *
         
# This port number in practice is often a "Well Known Number" 
serverPort = 11010

# create UDP socket and bind to your specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)

# The second parameter SOCK_DGRAM denotes that the connection is a UDP connection.
serverSocket.bind(("", serverPort))

# output to console that server is listening
print ("The Make Upper Case Server running over UDP is ready to receive ... ")
print("")
while 1:
    
    # read client's message AND REMEMBER client's address (IP and port)
    userInput, clientAddress = serverSocket.recvfrom(514)

    # converting the bytes to string format
    decodedMessage=userInput.decode('utf-8')

    # output to console the sentence received from client over UDP
    print ("The character(s) sent from client to server : ", decodedMessage)
    print("")
    
    # change client's sentence to upper case letters
    modifiedMessage = decodedMessage.upper()
	
    # send back modified sentence to the client using remembered address
    serverSocket.sendto(bytes(modifiedMessage, "UTF-8"), clientAddress)
    #connectionSocket.send(bytes(capitalizedSentence,"UTF-8"))
    # output to console the modified sentence sent back to client
    print ("The character(s) which is sent back from server : ", modifiedMessage)
    print("")
