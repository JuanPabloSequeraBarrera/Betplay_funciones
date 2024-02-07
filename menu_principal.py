import os
def MenuPrincipal():
    listopciones = [1,2,3,4,5]
    titulo = """
    ------------------------------------------
      +                                        +
    + BIENVENIDO AL SISTEMA DE PUNTOS FCF SA +
    +                                        +
    ------------------------------------------
    """
    os.system('cls')
    print (titulo)
    try: 
      opciones = ('1.Agregar equipo\n2. Registro de partidos\n3.Reportes de tabla de posiciones\n4. Tabla de posiciones\n5.Salir')
      print (opciones)
      op = int (input(':_)'))
      if not (op in listopciones):
        MenuPrincipal()
    except ValueError:
      print('Dato invalido')
      os.system('pause')
      MenuPrincipal()
    else:
      return op
          