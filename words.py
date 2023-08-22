def print_upper_words(words):
    """
    print out each word on a separate line
    but in all uppercase
    """
    for word in words:
        print(word.upper())

def print_upper_words_e(words):
    """
    only print words that start with the letter e 
    (either upper or lowercase)
    """
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())

def print_upper_words_3(words, must_start_with):
    """
    Make your function more general: you should be able to pass in 
    a set of letters and it only prints words that 
    start with one of those letters
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break