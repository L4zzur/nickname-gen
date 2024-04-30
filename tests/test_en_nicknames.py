import pytest

from nickname_gen.exceptions import (
    LangError,
    WordListAmountError,
    WordListNounAmountError,
    WordsAmountError,
    WordTypeError,
)
from nickname_gen.generator import Generator
from nickname_gen.wtypes import Lang, WordList, WordType


def test_generate_nickname() -> None:
    nickname = Generator.get_random_en_nickname()

    assert isinstance(nickname, str)


def test_generate_nickname_with_combos() -> None:
    combo_1 = WordList("combo 1", Lang.EN, ["smart", "good"], WordType.ADJECTIVE)
    combo_2 = WordList("combo 2", Lang.EN, ["dog", "cat"], WordType.NOUN)

    nickname = Generator.get_random_en_nickname(combos=[combo_1, combo_2])

    assert isinstance(nickname, str)


def test_generate_with_empty_combos() -> None:
    combo_1 = WordList("combo 1", Lang.EN, [], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.EN, [], WordType.ADJECTIVE)

    with pytest.raises(WordsAmountError):
        _ = Generator.get_random_en_nickname(combos=[combo_1, combo_2])


def test_generate_with_one_combo() -> None:
    combo_1 = WordList("combo 1", Lang.EN, [], WordType.NOUN)

    with pytest.raises(WordListAmountError):
        _ = Generator.get_random_en_nickname(combos=[combo_1])


def test_generate_without_combos() -> None:
    with pytest.raises(WordListAmountError):
        _ = Generator.get_random_en_nickname(combos=[])


def test_generate_without_nouns() -> None:
    combo_1 = WordList("combo 1", Lang.EN, ["smart", "good"], WordType.ADJECTIVE)
    combo_2 = WordList("combo 2", Lang.EN, ["smart", "good"], WordType.ADJECTIVE)

    with pytest.raises(WordTypeError):
        _ = Generator.get_random_en_nickname(combos=[combo_1, combo_2])


def test_generate_with_two_nouns() -> None:
    combo_1 = WordList("combo 1", Lang.EN, ["dog", "cat"], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.EN, ["dog", "cat"], WordType.NOUN)

    with pytest.raises(WordListNounAmountError):
        _ = Generator.get_random_en_nickname(combos=[combo_1, combo_2])


def test_generate_with_different_langs() -> None:
    combo_1 = WordList("combo 1", Lang.RU, ["dog", "cat"], WordType.NOUN)
    combo_2 = WordList("combo 2", Lang.EN, ["smart", "good"], WordType.ADJECTIVE)

    with pytest.raises(LangError):
        _ = Generator.get_random_en_nickname(combos=[combo_1, combo_2])
