
import math
def media(a):
    suma = 0
    resp = 0
    for elemento in a:
        suma = suma + elemento

    resp = suma /(len(a))
    return resp

def desvEstandar(a):
    resp = 0
    suma = 0
    lista = []
    i = 0
    m = media(a)
    for elemento in a:
        resp = elemento - m
        resp = resp**2
        lista.append(resp)
        i = i+1
    
    
    for elemento in lista:
        suma = suma + elemento

    desv = math.sqrt(suma/len(a))

    return round(desv, 4)

numeros = [1,5,10,15,20,25]

print(desvEstandar(numeros))



