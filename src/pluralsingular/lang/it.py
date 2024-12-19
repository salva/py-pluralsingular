import unicodedata

class PluralizerSingularizer:
    
    EXCEPTIONS = {
        'uomo': 'uomini',
        'bue': 'buoi',
        'dio': 'dei',
        'tempio': 'templi',
        'mano': 'mani',
    }

    REVERSE_EXCEPTIONS = {v: k for k, v in EXCEPTIONS.items()}

    @staticmethod
    def remove_accent(char: str) -> str:
        return unicodedata.normalize('NFD', char)[0]

    @staticmethod
    def pluralize(word: str) -> str:
        if word in PluralizerSingularizer.EXCEPTIONS:
            return PluralizerSingularizer.EXCEPTIONS[word]
        if word.endswith(('o')):
            return word[:-1] + 'i'
        elif word.endswith(('a')):
            return word[:-1] + 'e'
        elif word.endswith(('e')):
            return word[:-1] + 'i'
        else:
            return word + 'i'
    
    @staticmethod
    def singularize(word: str) -> str:
        if word in PluralizerSingularizer.REVERSE_EXCEPTIONS:
            return PluralizerSingularizer.REVERSE_EXCEPTIONS[word]
        if word.endswith(('i')) and len(word) > 1:
            if word[:-1].endswith(('o', 'e')):
                return word[:-1] + 'o'
            return word[:-1]  # Remove 'i'
        if word.endswith(('e')) and len(word) > 1:
            return word[:-1] + 'a'
        return word


if __name__ == "__main__":
    print(PluralizerSingularizer.pluralize("uomo"))  # 'uomini'
    print(PluralizerSingularizer.pluralize("bue"))  # 'buoi'
    print(PluralizerSingularizer.pluralize("dio"))  # 'dei'
    print(PluralizerSingularizer.pluralize("tempio"))  # 'templi'
    print(PluralizerSingularizer.singularize("uomini"))  # 'uomo'
    print(PluralizerSingularizer.singularize("buoi"))  # 'bue'
    print(PluralizerSingularizer.singularize("dei"))  # 'dio'
    print(PluralizerSingularizer.singularize("templi"))  # 'tempio'
