# Se puede llamar a todas las  funciones que contenga un archivo externo de python 
# únicamente es agregar el símbolo "*", este hace referencia a todas las funciones
# que encuentre en el archivo externo

from funciones import * #<--- Simbolo "*" importa todas las funciones del archivo

bienvenidaPrograma()

print(sumar(8, 6))
print(restar(4, 5))
print(multiplicar(6, 4))