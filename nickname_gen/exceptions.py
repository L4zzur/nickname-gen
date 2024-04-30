class LangError(Exception):
    """Raised when the language of the word list is not the same as the others."""

    pass


class WordListAmountError(Exception):
    """Raised when there are less than two word lists in the combo lists."""

    pass


class WordListNounAmountError(Exception):
    """Raised when there are more than one nouns in the combo lists."""

    pass


class WordsAmountError(Exception):
    """Raised when there are less than one word in the combo lists."""

    pass


class WordTypeError(Exception):
    """Raised when there are more than one nouns in the combo lists."""

    pass


class GenderNotFoundError(Exception):
    """Raised when the gender of the noun is not found."""

    pass
