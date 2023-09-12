import random


class Alphabet:
    def __init__(self, symbols):
        self.symbols = symbols

    def get_symbols(self):
        return self.symbols
    
    def generate_words(self, length_of_language):
        language = set()
        iterador_set = self.symbols
        alphabet_list = list(self.symbols)
        iterador_set_list = list(iterador_set)

        while len(language) < length_of_language:
            random_element = random.choice(alphabet_list)
            iterador_set_list_runner = 0
            length_iterator_set_list = len(iterador_set_list)
            while iterador_set_list_runner < length_iterator_set_list and len(language) < length_of_language:
                new_word = random_element + iterador_set_list[iterador_set_list_runner]
                if new_word not in language:
                    language.add(new_word)
                    iterador_set_list.append(new_word)
                iterador_set_list_runner = iterador_set_list_runner+1

        return language