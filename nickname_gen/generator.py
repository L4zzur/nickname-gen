import random
from enum import Enum

import pymorphy3  # type: ignore

from nickname_gen.exceptions import (
    GenderNotFoundError,
    LangError,
    WordListAmountError,
    WordListNounAmountError,
    WordsAmountError,
    WordTypeError,
)
from nickname_gen.words import (
    EN_ADJECTIVES_WORDS,
    EN_ANIMALS_WORDS,
    EN_COLORS_WORDS,
    RU_ADJECTIVES_WORDS,
    RU_ANIMALS_WORDS,
    RU_COLORS_WORDS,
)
from nickname_gen.wtypes import Lang, WordList, WordType


class StyleEnum(str, Enum):
    CAPITAL = "capital"
    UPPER = "upper"
    LOWER = "lower"


class Generator:
    @staticmethod
    def __check_combos(combos: list[WordList], lang: Lang) -> None:
        if len(combos) < 2:
            raise WordListAmountError("There must be at least two combo lists.")

        noun_check = False
        adjective_check = False

        for combo in combos:
            if len(combo) == 0:
                raise WordsAmountError("There must be at least one word in the list.")
            if combo.lang != lang:
                raise LangError(f"{combo.lang} in {combo} is not {lang}.")
            if combo.words_type == WordType.NOUN:
                if noun_check:
                    raise WordListNounAmountError(
                        "There must be only one noun combo list."
                    )
                noun_check = True
            elif combo.words_type == WordType.ADJECTIVE:
                adjective_check = True
            if combo.lang != lang:
                raise LangError(
                    f"All words lists must be in the same language ({lang})."
                )

        if not noun_check or not adjective_check:
            raise WordTypeError(
                "Among the list of words, "
                "at least two must contain nouns and adjectives."
            )

    @staticmethod
    def get_random_en_nickname(
        combos: list[WordList] | None = None,
        separator: str = " ",
        style: StyleEnum = StyleEnum.CAPITAL,
    ) -> str:
        """
        Generates a random english nickname.

        Args:
            combos (list[WordList], optional): List of combo parts. \
                Must be at least two and one of them with nouns. \
                Defaults to [ADJECTIVES, COLORS, ANIMALS].
            separator (str, optional): separator between parts. Defaults to " ".
            style (StyleEnum, optional): style of nickname. \
                Exists capital, upper, lower. \
                Defaults to StyleEnum.CAPITAL.

        Raises:
            WordsAmountError: if there are less than one word in the list.
            WordListAmountError: if there are less than two combo lists.
            WordListNounAmountError: if there is more than one noun combo list.
            LangError: if the combo lists have different languages.
            WordTypeError: if the combo lists do not contain nouns and adjectives.

        Returns:
            str: random english nickname, joined by separator
        """
        if combos is None:
            combos = [EN_ADJECTIVES_WORDS, EN_COLORS_WORDS, EN_ANIMALS_WORDS]
        Generator.__check_combos(combos, Lang.EN)
        combos.sort(key=lambda combo: combo.words_type.value)

        nickname = []
        for combo in combos:
            part = random.choice(combo.words)
            nickname.append(part)

        if style == StyleEnum.CAPITAL:
            nickname = [part.capitalize() for part in nickname]
        elif style == StyleEnum.UPPER:
            nickname = [part.upper() for part in nickname]
        elif style == StyleEnum.LOWER:
            nickname = [part.lower() for part in nickname]

        return separator.join(nickname)

    @staticmethod
    def get_random_ru_nickname(
        combos: list[WordList] | None = None,
        separator: str = " ",
        style: StyleEnum = StyleEnum.CAPITAL,
    ) -> str:
        """
        Generates a random russian nickname, considering the gender of the noun.

        Args:
            combos (list[WordList], optional): List of combo parts. \
                Must be at least two and one of them with nouns. \
                Defaults to [ADJECTIVES, COLORS, ANIMALS].
            separator (str, optional): separator between parts. Defaults to " ".
            style (StyleEnum, optional): style of nickname. \
                Exists capital, upper, lower. \
                Defaults to StyleEnum.CAPITAL.

        Raises:
            WordsAmountError: if there are less than one word in the list.
            WordListAmountError: if there are less than two combo lists.
            WordListNounAmountError: if there is more than one noun combo list.
            LangError: if the combo lists have different languages.
            WordTypeError: if the combo lists do not contain nouns and adjectives.
            GenderNotFoundError: if the gender of the noun cannot be determined.

        Returns:
            str: random russian nickname, joined by separator
        """
        if combos is None:
            combos = [RU_ADJECTIVES_WORDS, RU_COLORS_WORDS, RU_ANIMALS_WORDS]
        Generator.__check_combos(combos, Lang.RU)
        combos.sort(key=lambda combo: combo.words_type.value)

        morph = pymorphy3.MorphAnalyzer()
        nickname = []
        for combo in combos:
            part = random.choice(combo.words)
            nickname.append(part)

        noun = nickname[len(nickname) - 1]
        if "masc" in morph.parse(noun)[0].tag:  # type: ignore
            gender = "masc"
        elif "femn" in morph.parse(noun)[0].tag:  # type: ignore
            gender = "femn"
        else:
            raise GenderNotFoundError(f"Can't get gender of noun: {noun}.")

        for i in range(len(nickname) - 1):
            nickname[i] = (
                morph.parse(nickname[i])[0]
                .inflect({gender, "nomn"})  # type: ignore
                .word  # type: ignore
            )

        if style == StyleEnum.CAPITAL:
            nickname = [part.capitalize() for part in nickname]
        elif style == StyleEnum.UPPER:
            nickname = [part.upper() for part in nickname]
        elif style == StyleEnum.LOWER:
            nickname = [part.lower() for part in nickname]

        return separator.join(nickname)
