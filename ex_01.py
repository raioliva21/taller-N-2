"""
Ejericio 1

Dada un String que se forman de manera aleatoria, devuelva una nueva lista cuyo contenido sea igual
a la original pero de modo invertida. Ejemplo:
Ejemplo:
"Di buen dıa a Papa"
Devuelva
"Papa a dıa buen Di"
"""
#pide ingresar frase
texto = input("Ingrese cualquier frase: ")
#fragmentacion de cadena en palabras que la conforman
texto = texto.split()
try:
    type(texto) == str
except:
    print("Error, el tipo ingresado no corresponde a un string")
#se inicia sentencia for con uso de range
#variable i es utilizada como indice en lista 'texto[]' 
#variable 'indice_mayor' corresponde al indice maximo de lista 'texto[]'
#se comienza primer ciclo desde 'indice_mayor', variable 'i' dismiuye en una unidad por cada ciclo
#variable i no puede tener valor -1, tal que ciclo acabe con imprimir el elemento en 'texto[0]'
indice_mayor = len(texto) - 1
for i in range (indice_mayor,-1,-1):
    #se imprimen palabras en orden inverso a cadena ingresada por usuario
    #se usa "end=' '" para evitar salto de linea y que frase quede en horizontal
    print(f"{texto[i]}", end=' ')
#se realiza salto de linea para que frase no se junte con enunciados de la terminal
print()