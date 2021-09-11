"""
Realizar el juego del ahorcado.
Primero se debe ingresar la palabra a adivinar de hasta 10 caracteres. Luego se muestra por cada letra
un guion bajo para que el jugador sepa la cantidad de letras a adivinar. Se ir ́a ingresando una a una
las letras y si estas se encuentran en la palabra las deber ́a ir mostrando en el lugar correspondiente.
Por cada letra que no se encuentre en la palabra perder ́a una vida. El jugador dispondr ́a de 5 vidas
para intentar ganar el juego.

"""

#variable 'vidas' corresponde a las vidas del jugador
puntos = 0
vidas = 5
#usuario ingresa palabra
palabra = input("Ingrese palabra: ")
value = len(palabra)
if value > 10:
    print("La palabra ingresada supera las 10 letras, evite ingresar palabras de gran tamaño")
#se crea copia de 'palabra' para crear lista
palabra_type_list = palabra
#se pasa a lista str ingresado por usuario
palabra_type_list = list(palabra_type_list)
#se asigna limite para posterior sentencia for
# print(f"{palabra_type_list[1]}")
limite = len(palabra)
#se reemplazan elementos de lista por '_' en correspondencia el juego
for i in range (0,limite, 1):
    palabra_type_list[i] = '_'
    # print(f"{palabra_type_list[i]}")
while vidas >= 1 :
    letra = input("\nIngrese letra: ")
    try:
         letra.isalpha() is True
    except:
        print("Error, no se ha ingresado letra") 
    if letra in palabra:
        aux = palabra.find(letra)
        palabra_type_list[aux] = letra
        puntos += 1
        if limite == puntos:
            print("Enhorabuena, has ganado la partida")
            break
    else:
        vidas -= 1
        if vidas < 1:
            print("Lo siento, has perdido el juego")
            break
    for i in range(0, limite, 1):
        print(f"{palabra_type_list[i]}", end=' ')

