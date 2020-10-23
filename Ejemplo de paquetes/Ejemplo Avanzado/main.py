from Matematicas.aritmetica.Aritmetica import suma
from Matematicas.trigonometrica.Trigonometrica import seno
from Matematicas.estadistica.Estadistica import desvEstandar

print("Llamando al módulo de la subcarpeta aritmética")
print(suma(10232, 123123), "\n")

print("Llamando al módulo de la subcarpeta trigonometrica")
print(seno(56), "\n")

print("Llamando al módulo de la subcarpeta estadística")
print(desvEstandar([4,5,6,7,8,9]), "\n")