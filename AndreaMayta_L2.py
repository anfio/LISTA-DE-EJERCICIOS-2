#1). Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el
#número.

listanumeros=[["num1",40],["num2",13],["num3",25]]
print(type(listanumeros))

for elemento in listanumeros:

    residuode2=elemento[1]%2

    if residuode2==0:
        print("El siguiente numero es un numero par: ",elemento[0]) 

#2. Realizar un programa que dibuje un cuadrado en consola con * ,usando bucles .

lado=int(input("Ingrese el tamaño del lado: "))

for i in range(lado):
    for j in range(lado):
        print("* ",end="")
    print()

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

#4). Realizar un programa que inserte valores en una lista desde el 1 hasta el 100 saltando en
#2 en 2 . Ejemplo : [ 1,3 ,5 ,...]

a=list(range(1, 101, 2))
print("La lista es",a)

#5.Definir una función que multiplique 2 números mayores de cero
numero1=int(input("Ingrese su primer numero: "))
numero2=int(input("Ingrese su segundo numero: "))
def multiplicar(numero1,numero2):
    if numero1>0 and numero2>0:
        return (numero1*numero2)
print(multiplicar(numero1,numero2))

#6).Definir las siguientes funciones :
# saludar(nombre)
# realizarTarea(tarea)
# despedirse(nombre)
# *las funciones imprimen lo que se envía como parámetro

def saludar(name):
    print("Buenos tardes",name)
nombre="Alejandra"
saludar(nombre)

def realizarTarea(tarea):
    print("Tienes que ",tarea)
hacer="estudiar "
realizarTarea(hacer)

def despedirse(fullname):
    print("Hasta la proxima",fullname)
nombre="Ale"
despedirse(nombre)

#7). Definir una función que retorne el mayor valor al ingresar 2 números.

def mayor (numero1, numero2):
    if numero1>numero2:
        return (f"El numero mayor es: ",numero1)
    else:
        return (f"El numero mayor es: ",numero2)

print("INGRESE DOS NUMEROS")
a=float(input("Ingrese su primer numero: "))
b=float(input("Ingrese su segundo numero: "))
print(mayor(a,b))

#8. Definir una función que imprima los argumentos ingresados desde linea de comandos
#Nota: Usar import sys.argv => *args

import sys

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(sys.argv)

#9.Realizar una función que tenga por parámetro un lista de numeros y aumente cada
#elemento en +1

def aumentar(lista):    
    lista[0]=lista[0]+1
    lista[1]=lista[1]+1
    lista[2]=lista[2]+1
    lista[3]=lista[3]+1
    lista[4]=lista[4]+1
    lista[5]=lista[5]+1
    return lista

lista=[1,2,3,4,5,6]
resultado=aumentar(lista)
print(resultado)


#10.)Realizar un programa que realice las siguientes funciones de string al texto.
#-split
#-count
#-find
#-uppercase
#-lowercase
#texto=”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
#Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
#impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
#los mezcló de tal manera que logró hacer un libro de textos especimen.”

my_string = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."
print(my_string.split(sep=" "))
print(my_string.count("el"))
print(my_string.find("simplemente"))
print(my_string.upper())
print(my_string.lower())


#11.Definir los atributos y métodos de una de las siguientes clases.
#- Persona
#- Gato
#- Producto

class customer:
    pass
Andrea=customer()

Andrea.documento="72395530"
Andrea.ocupacion="estudiante"
Andrea.edad="19"
print(f"La persona Andrea tiene {Andrea.edad} años "
      f"con Nro de documento {Andrea.documento} "
      f" y de ocupacion {Andrea.ocupacion}")