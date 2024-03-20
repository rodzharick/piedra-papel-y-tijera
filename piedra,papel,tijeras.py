#programa para jugar piedra papel y tijeras
##para este juego utilizaremos la biblioteca random

from random import *

#input
print("------------piedra,papel,tijeras----------")
usuario = int(input("selecciones la opccion : 1 piedra, 2 papel,3 tijeras"))

#  variables de entrada y proceso
maquina = randint (1,3)

# processing
if usuario == 1:
    if maquina == 1:
        rta= "empate"
    elif maquina == 2:
        rta= "perdiste"
    else:
        rta = "ganaste"
elif usuario == 2:
    if maquina == 1:
        rta = "ganaste"
    elif maquina ==2:
        rta= "empate"
    else:
        rta= "perdiste"

# output
print("----------resulatdos----------")
print(" tu eleccion fue : ", 1)
print(" la  eleccion de la maquina fue: ",2)
print("------------")
print(rta)