import os
import menu_principal as m
import nchanges as o
os.system('cls')
equipos = []
nombre = 0
sistema_en_uso = True
nfecha = []
fecha_jueg = 0
sumaequipos = 0
division = 0
promedio = 0
while sistema_en_uso:
    os.system ('cls')
    op = m.MenuPrincipal()
    if (op == 1):
        o.equip(equipos)
    elif(op == 2):
        o.fecha(nfecha)
        o.assig(equipos)
    elif(op == 3):
        o.rep(equipos)
    elif (op ==4):
        sistema_en_uso = False
        print ('muchas gracias por hacer uso del sofware')
        os.system('pause')
    else:
        os.system('cls')
        print ('Digitacion de opcion no valida')
    os.system('pause')