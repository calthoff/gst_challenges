def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()
user_input = None
while True and user_input != "q":
    user_input = input("type a word or q to quit:")
    if user_input in english_words:
        print("{} is a valid word".format(user_input))
    else:
        print("{} is not a valid word".format(user_input))
