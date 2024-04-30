from nickname_gen.data.EN import ADJECTIVES as __EN_ADJECTIVES
from nickname_gen.data.EN import ANIMALS as __EN_ANIMALS
from nickname_gen.data.EN import COLORS as __EN_COLORS
from nickname_gen.data.RU import ADJECTIVES as __RU_ADJECTIVES
from nickname_gen.data.RU import ANIMALS as __RU_ANIMALS
from nickname_gen.data.RU import COLORS as __RU_COLORS
from nickname_gen.wtypes import Lang, WordList, WordType

RU_ANIMALS_WORDS = WordList(
    "Russian animal names", Lang.RU, __RU_ANIMALS, WordType.NOUN
)
RU_COLORS_WORDS = WordList(
    "Russian color names", Lang.RU, __RU_COLORS, WordType.ADJECTIVE
)
RU_ADJECTIVES_WORDS = WordList(
    "Russian adjectives", Lang.RU, __RU_ADJECTIVES, WordType.ADJECTIVE
)

EN_ANIMALS_WORDS = WordList(
    "English animal names", Lang.EN, __EN_ANIMALS, WordType.NOUN
)
EN_COLORS_WORDS = WordList(
    "English color names", Lang.EN, __EN_COLORS, WordType.ADJECTIVE
)
EN_ADJECTIVES_WORDS = WordList(
    "English adjectives", Lang.EN, __EN_ADJECTIVES, WordType.ADJECTIVE
)
