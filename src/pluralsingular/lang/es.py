import unicodedata

import re

class PluralizerSingularizer:
    """
    This module provides methods to pluralize and singularize Spanish words.

    Note: Corrections to the rules and exceptions are welcome. If you find any 
    incorrect behavior or have suggestions for improvement, please contribute.
    """

    COMMON_EXCEPTIONS = {
        'país': 'países',
        'luz': 'luces',
        'pez': 'peces',
        'crisis': 'crisis',
        'análisis': 'análisis',
        'dios': 'dioses',
        'menú': 'menús',
        'rubí': 'rubíes',
        'marroquí': 'marroquíes',
        'colibrí': 'colibríes',
        'tabú': 'tabúes',
        'bisturí': 'bisturíes',
        'sacacorchos': 'sacacorchos',
        'paraguas': 'paraguas',
        'tijeras': 'tijeras',
        'gafas': 'gafas',
        'el': 'los',
        'la': 'las',
        'mamá': 'mamás',
        'papá': 'papás',
        'sofá': 'sofás',
        'dominó': 'dominós',
        'jardín': 'jardines',
        'pais': 'paises',
        'coche': 'coches',
        'abdomen': 'abdómenes',
        'carácter': 'caracteres',
        'este': 'estes',
        'hoy': 'hoy',
        'imagen': 'imágenes',
        'oeste': 'oestes',
        'origen': 'orígenes',
        'por': 'pores',
        'volumen': 'volúmenes',
        'autobús': 'autobuses',
        'aire': 'aires',
        'alcalde': 'alcaldes',
        'avance': 'avances',
        'base': 'bases',
        'calle': 'calles',
        'carne': 'carnes',
        'cien': 'cienes',
        'cierre': 'cierres',
        'cine': 'cines',
        'clase': 'clases',
        'entre': 'entres',
        'gripe': 'gripes',
        'gris': 'gris',
        'informe': 'informes',
        'jueves': 'jueves',
        'llave': 'llaves',
        'lunes': 'lunes',
        'madre': 'madres',
        'miércoles': 'miércoles',
        'nieve': 'nieves',
        'noche': 'noches',
        'nueve': 'nueves',
        'orden': 'ordenes',
        'padre': 'padres',
        'porotos': 'porotos',
        'saltamontes': 'saltamontes',
        'sangre': 'sangres',
        'seis': 'seis',
        'tarde': 'tardes',
        'tigre': 'tigres',
        'tres': 'tres',
        'verde': 'verdes',
        'viernes': 'viernes',
        'ómnibus': 'ómnibus',
        'nupcias': 'nupcias',
        'fase': 'fases',
        'martes': 'martes',
    }

    PLURALIZE_EXCEPTIONS = {}
    SINGULARIZE_EXCEPTIONS = {}

    for singular, plural in COMMON_EXCEPTIONS.items():
        PLURALIZE_EXCEPTIONS.setdefault(singular, plural)
        SINGULARIZE_EXCEPTIONS.setdefault(plural, singular)

    @staticmethod
    def remove_accent(char: str) -> str:
        return unicodedata.normalize('NFD', char)[0]

    @staticmethod
    def pluralize(word: str) -> str:
        if word in PluralizerSingularizer.PLURALIZE_EXCEPTIONS:
            return PluralizerSingularizer.PLURALIZE_EXCEPTIONS[word]

        # Words endings that are unlikely to inflect.
        if word.endswith(("esis", "isis", "osis")):
            return word

        # Words ending in a vowel get -s: gato => gatos.
        if word.endswith(('a', 'e', 'é', 'i', 'o', 'u')):
            return word + "s"

        # Words ending in a stressed vowel get -s: hindú => hindúes.
        if word.endswith(('á', 'í', 'ó', 'ú')):
            return word + "es"

        # Words ending in -és get -eses: holandés => holandeses, autobús => autobuses.
        for (a, b) in (('ás', 'ases'), ('és', 'eses'), ('ís', 'ises'), ('ós', 'oses'), ('ús', 'uses')):
            if word.endswith(a):
                return word[:-2] + b

        # Words ending in -s preceded by an unstressed vowel: gafas => gafas.
        if word.endswith("s") and len(word) > 3 and word[-2] in ('a', 'e', 'i', 'o', 'u'):
            return word

        # Words ending in -z get -ces: luz => luces
        if word.endswith("z"):
            return word[:-1] + "ces"

        # Words that change vowel stress: graduación => graduaciones.
        for a, b in (("án", "anes"), ("én", "enes"),
                     ("ín", "ines"), ("ón", "ones"),
                     ("ún", "unes")):
            if word.endswith(a):
                return word[:-2] + b

        # Words ending in a consonant get -es.
        return word + "es"

    @staticmethod
    def singularize(word: str) -> str:

        if word in PluralizerSingularizer.SINGULARIZE_EXCEPTIONS:
            return PluralizerSingularizer.SINGULARIZE_EXCEPTIONS[word]

        if word.endswith("s"):
            if word.endswith("es"):
                if word[:-2].endswith(("br", "i", "j", "t", "zn")):
                    return word[:-1]

                # gestiones => gestión, ataques => ataque
                for a, b in (("anes", "án"), ("enes", "én"),
                             ("eses", "és"), ("ines", "ín"),
                             ("ones", "ón"), ("unes", "ún"),
                             ("ques", "que")):
                    if word.endswith(a):
                        # no monosyllables, no accents
                        if re.search(r'[aeiou]', word[:-4]) and not re.search(r'[áéíóú]', word[:-4]):
                            return word[:-4] + b
                        break

                # luces => luz
                if word.endswith("ces"):
                    return word[:-3] + "z"

                return word[:-2]

            # hipotesis => hipothesis
            if word.endswith(("asis", "esis", "isis", "osis")):
                return word

            # gatos => gato
            return word[:-1]

        return word

if __name__ == "__main__":
    print(PluralizerSingularizer.pluralize("flor"))
    print(PluralizerSingularizer.pluralize("luz"))
    print(PluralizerSingularizer.pluralize("país"))
    print(PluralizerSingularizer.pluralize("rey"))
    print(PluralizerSingularizer.pluralize("crisis"))
    print(PluralizerSingularizer.pluralize("pantalón"))
    print(PluralizerSingularizer.singularize("flores"))
    print(PluralizerSingularizer.singularize("luces"))
    print(PluralizerSingularizer.singularize("países"))
    print(PluralizerSingularizer.singularize("reyes"))
    print(PluralizerSingularizer.singularize("crisis"))
    print(PluralizerSingularizer.singularize("pantalones"))
