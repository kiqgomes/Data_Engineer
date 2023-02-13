import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()

s.bind((HOST,PORT))
print(f'Waiting Connection -> PORT {PORT}')
s.listen(5)
con, adr = s.accept()
print('Request received from {adr}')
print(con)

message = ['Olá 1','Olá 2','Já falei olá','Desisto....']

for m in message:
    con.send(bytes(m,'utf-8'))
    time.sleep(2)
con.close()
