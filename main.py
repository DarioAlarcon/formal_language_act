import random

def mezclar_elementos(entrada):
    nuevo_set = set()
    iterador_set = entrada
    entrada_lista = list(entrada)
    iterador_set_list = list(iterador_set)

    while len(nuevo_set) < 20:
        elementos_aleatorios1 = random.choice(entrada_lista)
        c = 0
        lenn = len(iterador_set_list)
        while c < lenn and len(nuevo_set) < 20:
            nuevo_elemento = elementos_aleatorios1[0] + iterador_set_list[c]
            if nuevo_elemento not in nuevo_set:
                nuevo_set.add(nuevo_elemento)
                iterador_set_list.append(nuevo_elemento)
            c = c+1

    return nuevo_set

def concatenar_lenguajes(lenguaje_1, lenguaje_2):
    lenguaje_concatenado = set()
    lenguaje_concatenado_list = list(lenguaje_concatenado)
    lenguaje_1_lista = list(lenguaje_1)
    lenguaje_2_lista = list(lenguaje_2)
    i1 = 0
    while i1 < len(lenguaje_1_lista):
        i2 = 0
        while i2< len(lenguaje_2_lista):
            nuevo_elemento= lenguaje_1_lista[i1]+lenguaje_2_lista[i2]
            lenguaje_concatenado_list.append(nuevo_elemento)
            i2 = i2+1
        i1 = i1+1
    return lenguaje_concatenado_list


def potencia_lenguaje(lenguaje):
    lenguaje_iterador = lenguaje
    iteraciones = 3
    cantidad_iteraciones = 0
    while cantidad_iteraciones<iteraciones:
        lenguaje_iterador= concatenar_lenguajes(lenguaje_1=lenguaje, lenguaje_2= lenguaje_iterador)
        cantidad_iteraciones+=1
    print(lenguaje_iterador)


def calcular_inversa_cadenas(conjunto):
    inversa = set()
    for cadena in conjunto:
        inversa.add(cadena[::-1])
    return inversa



def main():
    Alphabet1 = set(map(str, input("Ingrese la lista de simbolos de su primer alfabeto separados por espacios: ").split()))
    Alphabet2 = set(map(str, input("Ingrese la lista de simbolos de su segundo alfabeto separados por espacios: ").split()))
    print(Alphabet1)
    print(Alphabet2)
    Alphabet3 = Alphabet1 | Alphabet2
    print(Alphabet3)
    Alphabet3 = Alphabet1 & Alphabet2
    print(Alphabet3)
    Alphabet3 = Alphabet1 - Alphabet2
    print(Alphabet3)
    Alphabet4 = mezclar_elementos(Alphabet1)
    print("lenguaje 1")
    print(Alphabet4)
    Alphabet5 = mezclar_elementos(Alphabet2)
    print("lenguaje 2")
    print(Alphabet5)
    print("lenguaje concarena")
    print(concatenar_lenguajes(Alphabet4, Alphabet5))
    print(len(concatenar_lenguajes(Alphabet4, Alphabet5)))
    print(potencia_lenguaje(list(Alphabet1)))
    print(calcular_inversa_cadenas(Alphabet1))

main()