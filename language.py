class Language:
    def __init__(self, words):
        self.words = words

    def get_words(self):
        return self.words
    
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
