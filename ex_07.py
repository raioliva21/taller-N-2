"""
Problema de parecidos. Cree un programa que a partir de un ingreso de 5 palabras indique las dos
palabras que m ́as se parecen y las dos que menos se parecen. Una palabra es parecida cuando a lo
menos el 70 % de sus caracteres aparecen en otra palabra, caso contrario NO HAY PARECIDO.
TOSTADO y ASADO se parecen.
TOSTADO y PELOTA no se parecen.
TOSTADO tiene los caracteres T - O - S - A - D y ASADO tiene los caracteres A - S - D - O, como
se ve, la totalidad de caracteres de ASADO est ́an contenidos en TOSTADO, por lo que son parecidas.

"""
word = list()
palabra = list()
mismas_letras_entre_palabras = list()
aux = int

for i in range (0,5,1):
    palabra = input("Ingrese palabra: ")
    palabra[i] = palabra
    palabra[i] = list(palabra[i])
for a in range (0, 5, 1):
    for b in range (0, len(palabra[a]), 1):
        for c in range(0,5,1):
            if (a != c):
                if (palabra[a][b] == palabra[c][b]):
                    mismas_letras_entre_palabras[a][c] += 1
                    if (len(palabra[a]) > len(palabra[b])):
                        similitud = (mismas_letras_entre_palabras[a][c] / len(palabra[a])) * 100
                        if(similitud > 70):
                            if(similitud > 70):
                                if (len(palabra[a]) == b - 1):
                                    print(f"Hay alta similitud entre las palabras {palabra[a]} y {palabra[c]}")
                    if (len(palabra[a]) == len(palabra[b]) and aux == 0):
                        similitud = (mismas_letras_entre_palabras[a][c] / len(palabra[a])) * 100
                        if(similitud > 70):
                            if (len(palabra[a]) == b - 1):
                                print(f"Hay alta similitud entre las palabras {palabra[a]} y {palabra[c]}")
                                aux = 1
                        else:
                            if (len(palabra[a]) == b - 1):
                                print(f"No hay similitud entre las palabras {palabra[a]} y {palabra[c]}")
                                aux = 1
