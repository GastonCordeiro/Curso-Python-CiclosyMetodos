n = int(input("Ingrese un número para comenzar: \n"))
contain=""
for i in range(n+1):
    for j in range(i):
        contain += str(j+1)
    contain += "\n"     

print(contain)        