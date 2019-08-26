import string 
import sys

clave = sys.argv[1]
for i in range (len(clave)):
    for j in range (len(string.ascii_lowercase)):
        if string.ascii_lowercase [j] == clave [i]:
            print("se encontro la letra: "+ string.ascii_lowercase [j] )
            break
        else:
            print("no se encontro ", j , " recorrido abecedario")
