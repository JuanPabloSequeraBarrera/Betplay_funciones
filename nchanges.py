import os
def equip(equipos:list):
    local = str(input('Digite el nombre del equipo que quiere agregar '))
    equipos.append([local,0,0,0,0,0,0,0]) #esta linea de codigo le agrega un pj,pg... a cada uno de los equipos que se añada a la lista
    print ('su equipo ha sido registrado correctamente')
    os.system('pause')
def fecha(nfecha:list):
    fecha_juego = int (input('Ingerese el numero de fecha '))
    nfecha.append([fecha_juego])
def assig(equipos:list):
    local = str (input('Ingrese el nombre del equipo local '))
    marcador1 = int (input ('ingrese el numero de goles que marcó el equipo local '))
    visitante = str(input('Ingrese el nombre del equipo visitante '))
    marcador2 = int (input ('ingrese el numero de goles que marcó el equipo visitante '))
    for i,item in enumerate(equipos):
        if (local in item):
            if (marcador1>marcador2):
                item[1]+= 1
                item[2]+= 1
                item[3]+= marcador1
                item[4]+= marcador2
                item[7]+= 3
            if (marcador2>marcador1):
                item[4]+= marcador2
                item[5]+= 1
        elif (visitante in item):        
            if (marcador2>marcador1):
                item[1]+= 1
                item[2]+= 1
                item[3]+= marcador2
                item[4]+= marcador1
                item[7]+= 3
            if (marcador2<marcador1):
                item[1]+=1
                item[3]+= marcador2
                item[4]+= marcador1
                item[5]+= 1
        else:
            for l,item in enumerate (equipos):
                if (local in item) and (marcador1== marcador2):
                    item[1]+= 1
                    item[3]+=marcador1
                    item[4]+=marcador2
                    item[6]+= 1
                    item[7]+= 1
                elif (visitante in item) and (marcador1 ==marcador2):
                    item[1]+= 1
                    item[3]+=marcador2
                    item[4]+=marcador1
                    item[6]+= 1
                    item[7]+= 1

def rep(equipos:list):
    sumaequipos = 0
    division = 0  
    promedio = 0
    print ('Reporte de tabla de posciones')
    import os
    from tabulate import tabulate
    print(tabulate(equipos,headers=['Equipo','PJ','PG','GF','GC','PP','PE','TP']))
    for i,item in enumerate(equipos):
        for j in range(int(i+1),len(equipos),1):
            if (equipos[i][3] < equipos[j][3]):
                aux = equipos[i]
                equipos [i] =equipos [j]
                equipos[j] = aux
            mayorgol = equipos[0][0]    
            print (f'El equipo con mas goles fue {mayorgol} ')
            break

    for k,item in enumerate(equipos):
        for j in range(int(k+1),len(equipos),1):
            if (equipos[k][7] < equipos[k][7]):
                aux = equipos[k]
                equipos [k] =equipos [j]
                equipos[j] = aux
            mayorpuntos = equipos[0][0]    
            print (f'El equipo con mas puntos fue {mayorpuntos} ')
            break

    for s,item in enumerate(equipos):
        for j in range(int(s+1),len(equipos),1):
            if (equipos[s][2] < equipos[s][2]):
                aux = equipos[s]
                equipos [s] =equipos [j]
                equipos[j] = aux
            mayorpartidos = equipos[0][0]    
            print (f'El equipo que mas partidos gano fue {mayorpartidos} ')
            break

    for item in equipos:
        sumaequipos += item[4]
        division += 1
        promedio = sumaequipos/division
        print(f'El promedio de goles de los equipos fue {promedio}')