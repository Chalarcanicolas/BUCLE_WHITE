# BUCLE WHILE

import math 

número = int(input("Digite un número: "))

while número<0:
    print("Error el número no es valido")
    número = int(input("Digite un número: "))

print(f"\n su raiz cuadrada es: {(math.sqrt(número)):.2f}")