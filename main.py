from dialogs import spanish_dialogs

def main():
    Alphabet1_symbols = set(map(str, input(spanish_dialogs.obtain_first_alphabet_message).split()))
    Alphabet2_symbols = set(map(str, input(spanish_dialogs.obtain_second_alphabet_message).split()))
    starlock_symbols_number = int(input(spanish_dialogs.obtain_numbers_of_star_lock_message))
    words_of_language_number = int(input(spanish_dialogs.obtain_numbers_of_language_word_message))
    index_of_power_of_language = int(input(spanish_dialogs.obtain_power_language_number_message))
    print(Alphabet1_symbols)
    print(Alphabet2_symbols)
    print(starlock_symbols_number)
    print(words_of_language_number)
    print(index_of_power_of_language)
main()