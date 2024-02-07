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
    opciones = m.MenuPrincipal()
    if (opciones == 1):
        o.equip(equipos)
    elif(opciones == 2):
        o.fecha(nfecha)
        o.assig(equipos)
    elif(opciones == 3):    
        o.rep(equipos)
    elif(opciones == 4):
        o.tabla(equipos)
    elif (opciones ==5):
        sistema_en_uso = False
        print ('muchas gracias por hacer uso del sofware')
        os.system('pause')