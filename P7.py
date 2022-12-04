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