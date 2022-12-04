#2. Realizar un programa que dibuje un cuadrado en consola con * ,usando bucles .

lado=int(input("Ingrese el tamaño del lado: "))

for i in range(lado):
    for j in range(lado):
        print("* ",end="")
    print()
