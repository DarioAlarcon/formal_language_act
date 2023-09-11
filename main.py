import random

def generate_words(alphabet, length_of_language):
    language = set()
    iterador_set = alphabet
    alphabet_list = list(alphabet)
    iterador_set_list = list(iterador_set)

    while len(language) < length_of_language:
        random_element = random.choice(alphabet_list)
        print(random_element)
        iterador_set_list_runner = 0
        length_iterator_set_list = len(iterador_set_list)
        while iterador_set_list_runner < length_iterator_set_list and len(language) < length_of_language:
            new_word = random_element + iterador_set_list[iterador_set_list_runner]
            if new_word not in language:
                language.add(new_word)
                iterador_set_list.append(new_word)
            iterador_set_list_runner = iterador_set_list_runner+1

    return language

def concatenate_languages(language_1, language_2):
    language_concatenated = set()
    language_concatenated_list = list(language_concatenated)
    language_1_list = list(language_1)
    language_2_list = list(language_2)
    iterator_language_1 = 0
    while iterator_language_1 < len(language_1_list):
        iterator_language_2 = 0
        while iterator_language_2< len(language_2_list):
            new_concatenated_word = language_1_list[iterator_language_1]+language_2_list[iterator_language_2]
            language_concatenated_list.append(new_concatenated_word)
            iterator_language_2 = iterator_language_2+1
        iterator_language_1 = iterator_language_1+1
    return language_concatenated_list


def power_of_language(language, iterations):
    language_final = language
    numbers_of_iterations = 1
    while numbers_of_iterations<iterations:
        language_final= concatenate_languages(language, language_final)
        numbers_of_iterations+=1
    print(language_final)


def calculate_reverse(language):
    reverse = set()
    for word in language:
        reverse.add(word[::-1])
    return reverse

def union(set_1, set_2):
    set_final = set_1 | set_2
    return set_final

def intersection(set_1, set_2):
    set_final = set_1 & set_2
    return set_final

def diference(set_1, set_2):
    set_final = set_1 - set_2
    return set_final

def main():
    Alphabet1 = set(map(str, input("Ingrese la lista de simbolos de su primer alfabeto separados por espacios: ").split()))
    Alphabet2 = set(map(str, input("Ingrese la lista de simbolos de su segundo alfabeto separados por espacios: ").split()))
    print(Alphabet1)
    print(Alphabet2)
main()