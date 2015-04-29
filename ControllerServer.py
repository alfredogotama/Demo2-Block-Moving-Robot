import socket
import serial
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('', 10000)
sock.bind(server_address)

sock.listen(1)

connection, clientAddress = sock.accept() #Not sure if works

ser = serial.Serial("/dev/ttyACM0", 9600)

while True:
   connection.sendall("Insert car command here: (a b c d e f g h i j r s ")
   command = connnection.recv(5) #Not sure
   ser.write(str(command))

connection.close()
   
