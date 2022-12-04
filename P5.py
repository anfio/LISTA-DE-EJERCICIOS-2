#5.Definir una función que multiplique 2 números mayores de cero
numero1=int(input("Ingrese su primer numero: "))
numero2=int(input("Ingrese su segundo numero: "))
def multiplicar(numero1,numero2):
    if numero1>0 and numero2>0:
        return (numero1*numero2)
print(multiplicar(numero1,numero2))