"""
El siguiente String est ́a encriptado de mala manera a pesar que de todos modos sigue siendo un mensaje
incomprensible. Idea un m ́etodo para extraer el mensaje y gu ́ardalo en una variable llamada mensaje
y mostrar el valor de la variable en pantalla.
string = ¡XeXgXaXsXsXeXmX XtXeXrXcXeXsX XaX XsXiX XsXiXhXt”

"""
#asignacion de cadena predeterminada de nombre 'cadena_inicial'
cadena_inicial = "¡XeXgXaXsXsXeXmX XtXeXrXcXeXsX XaX XsXiX XsXiXhXt"
#se suprime todo caracter 'X' en  cadena inicial
mensaje = cadena_inicial.split("X")
#se inicia sentencia for con uso de range
#variable i es utilizada como indice en lista 'mensaje[]' 
#variable 'indice_mayor' corresponde al indice maximo de lista 'mensaje[]'
#se comienza primer ciclo desde 'indice_mayor', variable 'i' dismiuye en una unidad por cada ciclo
#ciclo acaba al ser 'i' = 0, tal que ciclo no acabe impriendo el caracter '¡' del elemento 'mensaje[0]'
indice_mayor = len(mensaje) - 1
for i in range (indice_mayor, 0, -1):
    #se imprimen letras a modo que mensaje oculto sea legible
    print(f"{mensaje[i]}", end=' ')
#se realiza salto de linea para que frase no se junte con enunciados de la terminal
print()

