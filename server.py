# Christopher Cao
# ch282858
# CNT4704, Fall 2022

import socket
import math

serverPort = 5328

# create socket and establish a connection with the client
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', serverPort))

# listen to at most 1 connection at a time
serverSocket.listen(1)

# server should be up and running and listening to the incoming connections
clientConnection, clientAddress = serverSocket.accept()
print("Connected by client on ", clientAddress)
userInput = ''

# begin program
while True:
    # take client input
    data = clientConnection.recv(1024)
    userInput = data.decode()
    
    # initialize variables
    inputList = userInput.split()
    operandX = inputList[0]
    operation = inputList[1]
    operandY = inputList[2]
    answer = 0
    x = float(operandX)
    y = float(operandY)
    
    # exit program
    if (x == 0) and (operation == "/") and (y == 0):
        print("Received question " + '"' + userInput + '"' + "; end the server program")
        break
    
    # invalid operation
    if (operation != "+") and (operation != "-") and (operation != "*") and (operation != "/"):
        answer = None
        output = str(answer)
        print("Received question " + '"' + userInput + '"' + "; send back error message")
        clientConnection.send(output.encode())
        
    # addition operation
    elif operation == "+":
        answer = x + y
        output = str(answer)
        print("Received question " + '"' + userInput + '"' + "; send back answer " + output)
        clientConnection.send(output.encode())
    
    # subtraction operation
    elif operation == "-":
        answer = x - y
        output = str(answer)
        print("Received question " + '"' + userInput + '"' + "; send back answer " + output)
        clientConnection.send(output.encode())
    
    # multiplication operation
    elif operation == "*":
        answer = x * y
        output = str(answer)
        print("Received question " + '"' + userInput + '"' + "; send back answer " + output)
        clientConnection.send(output.encode())
        
    # division operation
    elif operation == "/":
        answer = x / y
        output = str(answer)
        print("Received question " + '"' + userInput + '"' + "; send back answer " + output)
        clientConnection.send(output.encode())
    
clientConnection.close()
