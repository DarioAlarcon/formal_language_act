
def main():
    Alphabet1 = set(map(str, input("Ingrese la lista de simbolos de su primer alfabeto separados por espacios: ").split()))
    Alphabet2 = set(map(str, input("Ingrese la lista de simbolos de su segundo alfabeto separados por espacios: ").split()))
    print(Alphabet1)
    print(Alphabet2)
    Alphabet3 = Alphabet1 | Alphabet2 # union
    print(Alphabet3)
    Alphabet3 = Alphabet1 & Alphabet2 # union
    print(Alphabet3)
    Alphabet3 = Alphabet1 - Alphabet2 # union
    print(Alphabet3)



main()