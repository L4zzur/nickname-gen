# Nickname Generator
The Nickname Generator package provides simple functions to generate random nicknames.

## Installation
```bash
pip install nickname-gen
```

## Usage
This package provides two main methods for generating nicknames: `get_random_en_nickname` and `get_random_ru_nickname`.

### `get_random_en_nickname`

Generates a random nickname in English.

```python
from nickname_gen.generator import Generator
from nickname_gen.wtypes import WordList, WordType, Lang

# Using default parameters
nickname = Generator.get_random_en_nickname()
print(nickname)  # Example: 'Green Brave Tiger'

# Using a custom list of parts
my_adjectives = WordList("My Adjectives", Lang.EN, ["cool", "awesome"], WordType.ADJECTIVE)
my_nouns = WordList("My Nouns", Lang.EN, ["python", "developer"], WordType.NOUN)
nickname = Generator.get_random_en_nickname(combos=[my_adjectives, my_nouns])
print(nickname)  # Example: 'Awesome Developer'

# Using a custom separator
nickname = Generator.get_random_en_nickname(separator="-")
print(nickname)  # Example: 'Green-Brave-Tiger'

# Using a custom style
nickname = Generator.get_random_en_nickname(style=StyleEnum.UPPER)
print(nickname)  # Example: 'GREEN BRAVE TIGER'
```

This method can be customized by passing the following arguments:

- `combos` (`WordList` object, optional): a list of parts to compose the nickname. By default, it uses the lists of adjectives, colors, and animals in English.
- `separator` (string, optional): the separator between nickname parts. By default, it uses a space.
- `style` (`StyleEnum` instance, optional): the style of the nickname. By default, it uses `StyleEnum.CAPITAL`. Available options:
  - `StyleEnum.CAPITAL` (the first letter of each word is capitalized),
  - `StyleEnum.UPPER` (all letters are uppercase),
  - `StyleEnum.LOWER` (all letters are lowercase).

### `get_random_ru_nickname`

Generates a random nickname in Russian, considering the gender of the noun.

```python
from nickname_gen import Generator

# Using default parameters
nickname = Generator.get_random_ru_nickname()
print(nickname)  # Example: 'Зеленый Храбрый Тигр' ('Green Brave Tiger')

# Using custom parameters (similar to the English version)
...
```

This method can be customized by passing the same arguments as for `get_random_en_nickname`.

## Dependencies and Possible Errors
The `nickname_gen` library uses the following dependency:

- [`pymorphy3`](https://github.com/no-plagiarism/pymorphy3) - for determining the gender of the noun when generating Russian nicknames.

When using the `get_random_en_nickname` and `get_random_ru_nickname` methods, the following exceptions may occur:

- `WordsAmountError`: if there are fewer than one word in the list.
- `WordListAmountError`: if there are fewer than two elements in the list of combinations.
- `WordListNounAmountError`: if there is more than one list of nouns in the list of combinations.
- `LangError`: if the languages of the word lists in the combinations differ.
- `WordTypeError`: if the list of combinations does not contain lists of nouns and adjectives.
- `GenderNotFoundError`: if the gender of the noun could not be determined (for Russian language only).

## History and Inspiration
The idea for creating this package arose from the need to generate unique nicknames for one of my projects. Initially, I needed to generate random, but readable and memorable usernames.

Additional inspiration came from the user names and avatars that Google Docs assigns when collaborating on a document. They consist of an adjective and an animal name, such as "Unidentified Capybara," along with a random-colored icon of that animal. They are much more memorable than a set of random letters and numbers, but they do not accurately identify the user.

Based on this idea, I decided to create a package that would allow generating similar nicknames in different languages, while adding additional options to customize the format and style of the generated names, as well as the ability to use your own set of words. The result was the Nickname Generator package, which is now available for anyone to use.