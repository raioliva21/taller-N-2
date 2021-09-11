"""
Escriba un programa que indique si una palabra existe dentro de un texto. La palabra como la oraci ́on
ser ́an ingresadas por el usuario.

"""
#ingresa oracion
oracion = input("Ingrese una oracion cualquiera\n")
#control de excepcion 
if type(oracion) != str:
    print("El tipo de dato ingresado no corresponde a una cadena de caracteres\n")
else:
    #ingresa palabra a buscar
    palabra = input("Ingrese palabra que desea buscar dentro de la oracion recien ingresada\n")
    #control de excepcion
    if type(palabra) != str:
       print("El tipo de dato ingresado no corresponde a una cadena de caracteres\n")
    else:
        #para este caso, tambien se incluyen palabras implicitas dentro de otras palabras
        if palabra in oracion:
            print("La palabra buscada si existe dentro de la oracion\n")
        else:
            print("La palabra buscada no esta en la oracion\n")


