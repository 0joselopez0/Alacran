import pygame
import socket
import sys
import binascii
import math

#Diccionario del Joystick
def joystick_xyToDir(last_spd, eje_x, eje_y, num):
    global limitSpd
    x = eje_x
    y = eje_y
    x = 0 - x
    radius = math.sqrt(y * y + x * x)
    angle = math.atan2(y, x) * 180 / math.pi
    if angle < 0:
        angle += 360
    curr_spd = (radius - 0) * (limitSpd - 0) / (1 - 0) + 0
    if curr_spd > limitSpd:
        curr_spd = limitSpd
    if curr_spd != last_spd:
        if angle < 0 + 22.5 or angle >= 360 - 22.5:
            return str(num) + "W-" + str(int(curr_spd))
        if angle < 45 + 22.5:
            return str(num) + "H-" + str(int(curr_spd))
        if angle < 90 + 22.5:
            return str(num) + "S-" + str(int(curr_spd))
        if angle < 135 + 22.5:
            return str(num) + "A-" + str(int(curr_spd))
        if angle < 180 + 22.5:
            return str(num) + "E-" + str(int(curr_spd))
        if angle < 225 + 22.5:
            return str(num) + "C-" + str(int(curr_spd))
        if angle < 270 + 22.5:
            return str(num) + "N-" + str(int(curr_spd))
        if angle < 315 + 22.5:
            return str(num) + "G-" + str(int(curr_spd))


# Creando un socket TCP/IP

limitSpd = 60
last_spd = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket en el puerto cuando el servidor esté escuchando
def joystick_xyToDir2(last_spd2, eje_x, eje_y, num):
    global limitSpd2
    x = eje_x
    y = eje_y
    x = 0 - x
    radius = math.sqrt(y * y + x * x)
    angle = math.atan2(y, x) * 180 / math.pi
    if angle < 0:
        angle += 360
    curr_spd = (radius - 0) * (limitSpd2 - 0) / (1 - 0) + 0
    if curr_spd > limitSpd2:
        curr_spd = limitSpd2
    if curr_spd != last_spd2:
        if angle < 0 + 22.5 or angle >= 360 - 22.5:
            return str(num) + "W-" + str(int(curr_spd))
        if angle < 45 + 22.5:
            return str(num) + "H-" + str(int(curr_spd))
        if angle < 90 + 22.5:
            return str(num) + "S-" + str(int(curr_spd))
        if angle < 135 + 22.5:
            return str(num) + "A-" + str(int(curr_spd))
        if angle < 180 + 22.5:
            return str(num) + "E-" + str(int(curr_spd))
        if angle < 225 + 22.5:
            return str(num) + "C-" + str(int(curr_spd))
        if angle < 270 + 22.5:
            return str(num) + "N-" + str(int(curr_spd))
        if angle < 315 + 22.5:
            return str(num) + "G-" + str(int(curr_spd))

limitSpd2 = 99
last_spd2 = 60



pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

prevMsg = "00000"
server_address = ('192.168.31.106', 8080)

print(sys.stderr, 'conectando a %s puerto %s' % server_address)
sock.connect(server_address)
try:
    while True:
        # PROCESAMIENTO DEL EVENTO
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                hecho = True

        eje0 = joystick.get_axis(0)
        eje1 = joystick.get_axis(1)
        eje2 = joystick.get_axis(2)
        eje3 = joystick.get_axis(3)
        eje4 = joystick.get_axis(4)
        r1 = joystick.get_button(5)
        l1 = joystick.get_button(4)
        ba = joystick.get_button(0)
        bb = joystick.get_button(1)
        bx = joystick.get_button(2)
        by = joystick.get_button(3)
        start = joystick.get_button(7)
        select = joystick.get_button(6)

        if eje1 > 0.4 or eje1 < -0.4 or eje0 > 0.4 or eje0 < -0.4:
            message = joystick_xyToDir(last_spd, eje0, eje1, 1)
        elif eje3 > 0.4 or eje3 < -0.4 or eje4 > 0.4 or eje4 < -0.4:
            message = joystick_xyToDir2(last_spd2, eje4, eje3, 2)
        elif r1:
            message = "R1111"
        elif l1:
            message = "L1111"
        elif ba:
            message = "BAAAA"
        elif bb:
            message = "BBBBB"
        elif bx:
            message = "BXXXX"
        elif by:
            message = "BYYYY"
        elif start:
            message = "STTTT"
        elif select:
            message = "SLLLL"
        elif eje2 > 0.1:
            if eje2 > 1:
                ejefinal = 50
            else:
                ejefinal = int(eje2 * 50)
            message = "L2-" + str(ejefinal)
        elif eje2 < -0.1:
            if eje2 < -1:
                ejefinal = -50
            else:
                ejefinal = int(eje2 * -50)
            message = "R2-" + str(ejefinal)
        else:
            message = "00000"
        if prevMsg != message:
            prevMsg = message
            message = message.encode()
            sock.send(message)
            print(message)

# Corregir pinza - corregido con dos botones
# Cuando giro / pinza se mueve
# Algo raro con movimiento normal

finally:
    print(sys.stderr, 'cerrando socket')
    sock.close()
