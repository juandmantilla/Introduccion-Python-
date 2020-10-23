
# Los paquetes en python permiten ordenar los módulos que estén
# almacenados en ficheros o carpetas

# Cree un archivo vació llamado __init__ en una carpeta contenedora. En esta carpeta
# agregará los archivos que deseen estar en el contenedor. Seguidamente puede hacer
# referencia a las funciones desde otro archivo externo.


#Importar funciones que se encuentra en la carpeta "calculos"

from calculos.funciones import potencia #<-- Llame primero a la carpeta contenedora. Seguidamente haga referencia a la función que desee importar

print("Uso de función potencia desde contenedor")
print(potencia(2, 34))

