"""
Escriba un programa que pida al usuario dos palabras, y se indique cu ́al de ellas es la m ́as larga y por
cu ́antas letras lo es.

"""
#se pide a usuario ingresar dos palabras por separado
primera_palabra = input("Ingrese una primera palabra\n")
segunda_palabra = input("Ingrese una segunda palabra\n")
#control de excepcion
if type(primera_palabra) != str or type(segunda_palabra) != str:
    print("El tipo de variable ingresado no corresponde a cadena")
#variable a la que se asigna valor corresponde a la diferencia de longuitud (letras) entre las palabras ingresadas por usuario
diferencia_len_palabras = len(primera_palabra) - len(segunda_palabra)
if type(diferencia_len_palabras) != int:
    print("El tipo de variable correspondiente a la diferencia entre longuitud de primera y segunda palabra no es entero")
#si primera palabra es mas larga que segunda palabra
if diferencia_len_palabras > 0:
    print("La primera palabra es mas larga que la segunda palabra por", diferencia_len_palabras,"letras")
#si segunda palabra es mas larga que primera palabra
elif diferencia_len_palabras == 0:
    print("Ambas palabras tienen la misma cantidad de letras, tal que no hay palabra mas larga que otra")
#si ambas palabras tienen el mismo tamaño 
else:
    diferencia_len_palabras *= -1
    print("La segunda palabra es mas larga que la segunda palabra por", diferencia_len_palabras,"letras")
