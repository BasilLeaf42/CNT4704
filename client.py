# Christopher Cao
# ch282858
# CNT4704, Fall 2022

import socket
import math

serverName = "eustis3.eecs.ucf.edu"
serverPort = 5328

# create socket and establish a connection with the server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Connected with server on " + serverName)

# begin program
while True:
    # take user input
    userInput = input()
    inputList = userInput.split(" ")
    
    # verify that the operand values are valid
    if (inputList[0].replace(".", "").isnumeric()) and (inputList[2].replace(".", "").isnumeric()):
        # check for the prompt to exit the program; we don't terminate immediately because we need to inform the server
        if (inputList[0] == "0") and (inputList[1] == "/") and (inputList[2] == "0"):
            print("User input ends; end the client program")
            
            # send the userInput to the server; it will terminate after discovering that the input is the prompt to exit
            clientSocket.send(userInput.encode())
            
            # break after the server process gets the message to terminate
            break
            
        else:
            # send the userInput to the server
            clientSocket.send(userInput.encode())
            
            # receive answer from the server and output to the user
            answer = clientSocket.recv(1024)
            
            # print out error message for invalid operator
            if answer.decode() == 'None':
                print("Input error. Re-type the math question again.")
                
            # print out answer for valid equation
            else:
                print("Answer from server: " + answer.decode())
    
    # return if the operand values are invalid
    else:
        print("Input error. Re-type the math question again.")
    
clientSocket.close()
