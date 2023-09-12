from dialogs import spanish_dialogs
from alphabet import Alphabet
from funtions import union, intersection, diference
from language import Language, concatenate_languages, power_of_language, calculate_reverse

def main():
    alphabet1_symbols = set(map(str, input(spanish_dialogs.obtain_first_alphabet_message).split()))
    alphabet_1 = Alphabet(alphabet1_symbols)
    alphabet2_symbols = set(map(str, input(spanish_dialogs.obtain_second_alphabet_message).split()))
    alphabet_2 = Alphabet(alphabet2_symbols)
    starlock_symbols_number = int(input(spanish_dialogs.obtain_numbers_of_star_lock_message))
    words_of_language_number = int(input(spanish_dialogs.obtain_numbers_of_language_word_message))
    #index_of_power_of_language = int(input(spanish_dialogs.obtain_power_language_number_message))
    print(spanish_dialogs.result_first_alphabet_message)
    print(alphabet_1.get_symbols())
    print(spanish_dialogs.result_second_alphabet_message)
    print(alphabet_2.get_symbols())
    print(spanish_dialogs.result_union_alphabets_message)
    print(union(alphabet_1.get_symbols(),alphabet_2.get_symbols()))
    print(spanish_dialogs.result_intersection_alphabets_message)
    print(intersection(alphabet_1.get_symbols(),alphabet_2.get_symbols()))
    print(spanish_dialogs.result_diference_alphabets_message)
    print(diference(alphabet_1.get_symbols(),alphabet_2.get_symbols()))
    print(spanish_dialogs.result_starlock_alphabets_message)
    print(alphabet_1.generate_words(starlock_symbols_number))
    print(alphabet_2.generate_words(starlock_symbols_number))
    print(spanish_dialogs.result_first_language_message)
    language_1 = Language(alphabet_1.generate_words(words_of_language_number))
    print(language_1.get_words())
    print(spanish_dialogs.result_second_language_message)
    language_2 = Language(alphabet_2.generate_words(words_of_language_number))
    print(language_2.get_words())
    


main()