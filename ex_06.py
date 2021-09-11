"""
Cree un programa que permita concatenar los datos o palabras ingresadas por un usuario. El ingreso
de palabras debe estar controlado por un ciclo y cuando se escriba la palabra fin termine la ejecuci ́on
y se muestren todos los datos ingresados de forma concatenada

"""
#asigna tipo a variable 'palabra'
palabra = str
#asigna caracter nulo a 'union'
union = ""
#asigna valor 0 a 'i' antes de ingresar a ciclo
i = 0
#ciclo acaba cuando se ingresa cadena = 'fin'
while i != 'fin':
    #se aumenta una unidad en 'i' por cada ciclo
    i+=1
    #se registra palabra en variable 'palabra'
    palabra = input("Ingrese dato(s)/palabra(s): ")
    #cada elemento de cadena queda en minuscula
    palabra.lower()
    #si palabra ingresada es 'fin'
    if palabra == 'fin':
        #acaba ciclo
        break
    #se concatenan palabras en variable 'union'
    union += palabra + " "
#se imprime variable union
print(f"{union}")