'''
Sam Bergin 170670850
Adam Joe 170801790
'''
# Import socket module

import sys # In order to terminate the program
import time
import pickle
from socket import *

print("1-connect")
print("2-disconnect")
print("3-POST")
print("4-GET")
print("5-PIN")
print("6-UNPIN")
print("7-CLEAR")
while True:
    userIn = input("Enter a Number to perform:")
    if(userIn == '1'):
        serverName = input("Enter Server Name:")
        serverPort = int(input("Enter Server Port:"))
        clientSocket = socket(AF_INET, SOCK_STREAM)

        clientSocket.connect((serverName, serverPort))

    elif(userIn == '2'):
        print("disconnected")
        post = '2'
        clientSocket.send(post.encode())
        clientSocket.close()
        break
            

    elif(userIn == '3'):
        coordx = input('Input x coordinate: ')
        coordy = input('Input y coordinate: ')
        width = input('Enter the width of this note: ')
        height = input('Enter the height of this note: ')
        color = input('Enter the color of this note: ')
        sentence = input(' Input the message for the note: ')
        if(coordx.isnumeric() and coordy.isnumeric() and width.isnumeric()and height.isnumeric()):
            post = '3' + " " + coordx + " " + coordy  + " " + width + " " + height + " " + color + " " + sentence
            print(post)
            
            clientSocket.send(post.encode())
        else:
            print("please insert numeric values where required.")
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
        
    elif(userIn == '4'):
        coordx = input('Input x coordinate(input None if unwanted): ')
        coordy = input('Input y coordinate(input None if unwanted): ')
        color = input('Enter the color of this note(input None if unwanted): ')
        sentence = input(' Input the message for the note(input None if unwanted): ')
        if(coordx.isnumeric() and coordy.isnumeric()):
            get = '4' + " " + coordx + " " + coordy  + " "  + color + " " + sentence
            
            clientSocket.send(get.encode())
        else:
            print("please insert numeric values where required.")
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
        
    elif(userIn == '5'):
        coordx = input('Input the x coordinate of the note you would like to pin: ')
        coordy = input('Input the y coordinate of the note you would like to pin: ')
        if(coordx.isnumeric() and coordy.isnumeric()):
            pin = '5' + " " + coordx + " " + coordy
            
            clientSocket.send(pin.encode())
        else:
            print("please insert numeric values where required.")
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
    elif(userIn == '6'):
        coordx = input('Input the x coordinate of the note you would like to unpin: ')
        coordy = input('Input the y coordinate of the note you would like to unpin: ')
        if(coordx.isnumeric() and coordy.isnumeric()):
            pin = '6' + " " + coordx + " " + coordy
            
            clientSocket.send(pin.encode())
        else:
            print("please insert numeric values where required.")
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode()) 
    
    elif(userIn =='7'):
        pin = '7'
        clientSocket.send(pin.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From server: ', modifiedSentence.decode())
           

    else:
        print("else")

#serverName = 'localhost'
# Assign a port number
#serverPort = 6789