from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    f = open(DICTIONARY, 'r')
    return [line.rstrip() for line in f]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        score += LETTER_SCORES.get(letter.upper(), 0)
    return score


def max_word_value(words=()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    max_value = 0
    max_word = None
    for word in words:
        value = calc_word_value(word)
        if max_value < value:
            max_value = value
            max_word = word
    return max_word


if __name__ == "__main__":
    pass
