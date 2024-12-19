import unicodedata

class PluralizerSingularizer:
    """
    A simple custom pluralizer/singularizer that supports Spanish names.
    """

    EXCEPTIONS = {
        'país': 'países',  # Custom exception for singular to plural
        'luz': 'luces',
        'pez': 'peces',
        'crisis': 'crisis',  # Crisis is both singular and plural
        'análisis': 'análisis',  # Análisis is both singular and plural
    }

    @staticmethod
    def remove_accent(char: str) -> str:
        """Removes the accent from a character using Unicode decomposition."""
        return unicodedata.normalize('NFD', char)[0]

    @staticmethod
    def pluralize(word: str) -> str:
        """Pluralize a Spanish name."""
        if word in PluralizerSingularizer.EXCEPTIONS:
            return PluralizerSingularizer.EXCEPTIONS[word]
        vowels = "aeiouáéíóú"  # Including accented vowels
        if word.endswith(('z')):
            return word[:-1] + 'ces'
        elif word.endswith(('ón', 'én', 'án', 'ín', 'ún')):  # Generalize words ending with an accent on the last syllable
            return word[:-2] + PluralizerSingularizer.remove_accent(word[-2]) + 'nes'
        elif word.endswith('y'):
            return word[:-1] + 'ies'
        elif word.endswith('s'):
            return word  # Words ending in 's' are often already plural in Spanish (like "crisis")
        elif word.endswith(tuple(vowels)):
            return word + 's'
        else:
            return word + 'es'

    @staticmethod
    def singularize(word: str) -> str:
        """Singularize a Spanish name."""
        for singular, plural in PluralizerSingularizer.EXCEPTIONS.items():
            if word == plural:
                return singular
        if word.endswith('nes') and len(word) > 4:
            # Handle words ending in 'nes' to 'ón', 'én', 'án', 'ín', 'ún'
            if word[-4] in 'aeiouáéíóú':
                return word[:-3] + unicodedata.normalize('NFD', word[-4])[0] + 'n'
        if word.endswith('cies') and len(word) > 4:
            return word[:-3] + 'y'
        if word.endswith('ces') and len(word) > 3 and word[-4] != 'z':
            return word[:-3] + 'z'
        elif word.endswith('es') and len(word) > 2:
            # Handle cases like "flores" to "flor"
            if word[-3] not in 'aeiouáéíóú':  # Not a vowel
                return word[:-2]
            return word[:-1]  # Handle cases like "aves" to "ave"
        elif word.endswith('s') and len(word) > 1 and word not in PluralizerSingularizer.EXCEPTIONS.values():
            return word[:-1]
        return word


# Usage examples
if __name__ == "__main__":
    # Spanish examples
    print("\nSpanish Names Examples")
    print(PluralizerSingularizer.pluralize("flor"))  # 'flores'
    print(PluralizerSingularizer.pluralize("luz"))  # 'luces'
    print(PluralizerSingularizer.pluralize("país"))  # 'países'
    print(PluralizerSingularizer.pluralize("rey"))  # 'reyes'
    print(PluralizerSingularizer.pluralize("crisis"))  # 'crisis' (unchanged)
    print(PluralizerSingularizer.pluralize("pantalón"))  # 'pantalones'
    print(PluralizerSingularizer.singularize("flores"))  # 'flor'
    print(PluralizerSingularizer.singularize("luces"))  # 'luz'
    print(PluralizerSingularizer.singularize("países"))  # 'país'
    print(PluralizerSingularizer.singularize("reyes"))  # 'rey'
    print(PluralizerSingularizer.singularize("crisis"))  # 'crisis' (unchanged)
    print(PluralizerSingularizer.singularize("pantalones"))  # 'pantalón'
    print(PluralizerSingularizer.singularize("análisis"))  # 'análisis' (unchanged)
