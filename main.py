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
        while c < lenn:
            nuevo_elemento = elementos_aleatorios1[0] + iterador_set_list[c]
            if nuevo_elemento not in nuevo_set:
                nuevo_set.add(nuevo_elemento)
                iterador_set_list.append(nuevo_elemento)
            c = c+1

    return nuevo_set

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
    print(mezclar_elementos(Alphabet1))

main()