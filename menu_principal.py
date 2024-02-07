import os
def MenuPrincipal()->int:
    op = '1.Agregar equipo\n2. Registro de partidos\n3.Reportes de tabla de posciones\n4.Salir'
    titulo = """
    ------------------------------------------
      +                                        +
    + BIENVENIDO AL SISTEMA DE PUNTOS FCF SA +
    +                                        +
    ------------------------------------------
    """
    print (titulo)
    print (op)
    op = int (input(':_)'))
    return op
          