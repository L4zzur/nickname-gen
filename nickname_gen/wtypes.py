from enum import Enum


class WordType(str, Enum):
    NOUN = "noun"
    ADJECTIVE = "adjective"


class Lang(str, Enum):
    RU = "ru"
    EN = "en"


class StyleEnum(str, Enum):
    CAPITAL = "capital"
    UPPER = "upper"
    LOWER = "lower"


class WordList:
    def __init__(
        self, name: str, lang: Lang, words: list[str], words_type: WordType
    ) -> None:
        self.name = name
        self.lang = lang
        self.words = words
        self.words_type = words_type

    def __repr__(self) -> str:
        return f"WordList({self.name}, {self.lang}, {self.words_type})"

    def __len__(self) -> int:
        return len(self.words)
