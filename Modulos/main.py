# Para llamar a las funciones de otro archivo .py
# es necesario hacer referencia al nombre de archivo que se desee ejecutar

# La palabra reservada import permite hacer el llamado a las funciones presentes en el 
# archivo especificado

import  funciones

funciones.bienvenidaPrograma()

print("Ejecutando funciones del archivo funciones.py")
print(funciones.sumar(12, 20))
print(funciones.restar(20,45))
print(funciones.multiplicar(34, 12))


