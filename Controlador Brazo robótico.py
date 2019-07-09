import socket
import sys
import time

# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket en el puerto cuando el servidor esté escuchando
# server_address = ('localhost', 10000)

server_address = ('192.168.31.106', 8081)
# server_address = ('192.168.31.247', 8080)

print(sys.stderr, 'conectando a %s puerto %s' % server_address)
sock.connect(server_address)  #conectado
try:
    while True:
        print('Introduce un comando: ')
        message = input()

        message = message.encode()
        sock.sendall(message)
        # Buscando respuesta

        amount_received = 0
        amount_expected = len(message)

#Lectura de comandos

finally:
    print(sys.stderr, 'cerrando socket')
    sock.close()
# G1 X10 F500
# G91 X10 F500
