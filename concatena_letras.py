from string import ascii_lowercase
import math
def gen(cant):
    tmp = math.ceil(cant / len(ascii_lowercase)) * ascii_lowercase
    cont = 0
    letras = " "
    while cont < cant:
        letras += tmp[cont]
        cont += 1
    print(letras)

gen(100)    