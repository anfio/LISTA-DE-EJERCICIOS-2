#3.Realizar un programa que dibuje un triángulo en consola con * ,usando bucles
altura=int(input("Ingrese la altura del triangulo: "))

for i in range(1,altura+1):
    for j in range(altura-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(1,i):
        print("*",end="")
    print()
