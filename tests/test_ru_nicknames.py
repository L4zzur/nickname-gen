import pytest

from nickname_gen.exceptions import (
    GenderNotFoundError,
    LangError,
    WordListAmountError,
    WordListNounAmountError,
    WordsAmountError,
    WordTypeError,
)
from nickname_gen.generator import Generator
from nickname_gen.wtypes import Lang, WordList, WordType


def test_generate_nickname() -> None:
    nickname = Generator.get_random_ru_nickname()

    assert isinstance(nickname, str)


def test_generate_nickname_with_combos() -> None:
    combo_1 = WordList("combo 1", Lang.RU, ["умный", "хороший"], WordType.ADJECTIVE)
    combo_2 = WordList("combo 2", Lang.RU, ["собака", "кошка"], WordType.NOUN)

    nickname = Generator.get_random_ru_nickname(combos=[combo_1, combo_2])

    assert isinstance(nickname, str)


def test_generate_with_empty_combos() -> None:
    combo_1 = WordList("combo 1", Lang.RU, [], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.RU, [], WordType.ADJECTIVE)

    with pytest.raises(WordsAmountError):
        _ = Generator.get_random_ru_nickname(combos=[combo_1, combo_2])


def test_generate_with_one_combo() -> None:
    combo_1 = WordList("combo 1", Lang.RU, [], WordType.NOUN)

    with pytest.raises(WordListAmountError):
        _ = Generator.get_random_ru_nickname(combos=[combo_1])


def test_generate_without_combos() -> None:
    with pytest.raises(WordListAmountError):
        _ = Generator.get_random_ru_nickname(combos=[])


def test_generate_without_nouns() -> None:
    combo_1 = WordList("combo 1", Lang.RU, ["умный", "хороший"], WordType.ADJECTIVE)
    combo_2 = WordList("combo 2", Lang.RU, ["умный", "хороший"], WordType.ADJECTIVE)

    with pytest.raises(WordTypeError):
        _ = Generator.get_random_ru_nickname(combos=[combo_1, combo_2])


def test_generate_with_two_nouns() -> None:
    combo_1 = WordList("combo 1", Lang.RU, ["собака", "кошка"], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.RU, ["собака", "кошка"], WordType.NOUN)

    with pytest.raises(WordListNounAmountError):
        _ = Generator.get_random_ru_nickname(combos=[combo_1, combo_2])


def test_generate_with_different_langs() -> None:
    combo_1 = WordList("combo 1", Lang.RU, ["собака", "кошка"], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.EN, ["good", "smart"], WordType.ADJECTIVE)

    with pytest.raises(LangError):
        _ = Generator.get_random_ru_nickname(combos=[combo_1, combo_2])


def test_generate_with_unknown_gender() -> None:
    combo_1 = WordList("combo 1", Lang.RU, ["сорока", "сорока"], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.RU, ["умный", "хороший"], WordType.ADJECTIVE)

    with pytest.raises(GenderNotFoundError):
        _ = Generator.get_random_ru_nickname(combos=[combo_1, combo_2])
