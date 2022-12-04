#1). Realizar una iteración de una lista de números e identificar si es múltiplo de 2 e imprimir el
#número.

listanumeros=[["num1",40],["num2",13],["num3",25]]
print(type(listanumeros))

for elemento in listanumeros:

    residuode2=elemento[1]%2

    if residuode2==0:
        print("El siguiente numero es un numero par: ",elemento[0]) 
