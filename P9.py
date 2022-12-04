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
