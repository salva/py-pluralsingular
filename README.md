# PluralSingular

**PluralSingular** is a Python module that provides functionality to pluralize and singularize words in multiple languages. Currently, it supports both **Spanish** and **English** through dedicated backends. The module follows a simple interface to make it easy to add support for additional languages.

> **Note:** This is an early release of the module. Contributions, corrections, support for other language backends, and any form of feedback are highly welcome.

## 📦 **Installation**
```bash
pip install pluralsingular
```

---

## 🚀 **Usage**
To use **PluralSingular**, you can import the main functions directly from the package:

```python
from pluralsingular import pluralize, singularize

# Pluralize and singularize in English (default language)
print(pluralize("dog"))  # 'dogs'
print(singularize("dogs"))  # 'dog'

# Pluralize and singularize in Spanish
print(pluralize("flor", lang="es"))  # 'flores'
print(singularize("flores", lang="es"))  # 'flor'
```

---

## 🔧 **Functions**

### `pluralize(word: str, lang: str = 'en') -> str`
Pluralizes a given word based on the specified language.

**Arguments:**
- `word` (str): The word to be pluralized.
- `lang` (str, optional): The language to be used for pluralization (default is 'en').

**Returns:**
- `str`: The pluralized form of the word.

**Example:**
```python
print(pluralize("dog"))  # 'dogs'
print(pluralize("futbol", lang="es"))  # 'futboles'
```

---

### `singularize(word: str, lang: str = 'en') -> str`
Singularizes a given word based on the specified language.

**Arguments:**
- `word` (str): The word to be singularized.
- `lang` (str, optional): The language to be used for singularization (default is 'en').

**Returns:**
- `str`: The singularized form of the word.

**Example:**
```python
print(singularize("dogs"))  # 'dog'
print(singularize("futboles", lang="es"))  # 'futbol'
```

---

## 🌍 **Supported Languages**
The following languages are supported:
- **English** (default, implemented using the `inflect` package)
- **Spanish** (custom implementation using language-specific rules)

Each language has its own backend, and new languages can be added by following the structure in `pluralsingular/lang/`.

---

## 🤔 **How It Works**
The module dynamically loads the appropriate backend for each language when the `pluralize` or `singularize` function is called. The backends are cached to avoid multiple imports. Each backend implements the same interface with two methods:
- **`pluralize(word: str) -> str`**
- **`singularize(word: str) -> str`**

The **Spanish backend** uses a set of rules and exceptions to handle irregular forms, while the **English backend** relies on the `inflect` package for robust pluralization and singularization.

---

## ✨ **Features**
- **Multi-language support**: Handle multiple languages with ease.
- **Custom backends**: Easily extend the package to support other languages.
- **Dynamic imports**: Load only what is needed for each language.
- **Exception handling**: Custom handling for irregular words.

---

## 📚 **Examples**

### **Spanish Examples**
```python
from pluralsingular import pluralize, singularize

print(pluralize("flor", lang="es"))  # 'flores'
print(pluralize("luz", lang="es"))  # 'luces'
print(pluralize("país", lang="es"))  # 'países'
print(pluralize("rey", lang="es"))  # 'reyes'

print(singularize("flores", lang="es"))  # 'flor'
print(singularize("luces", lang="es"))  # 'luz'
print(singularize("países", lang="es"))  # 'país'
print(singularize("reyes", lang="es"))  # 'rey'
```

---

## 🛠️ **Development**
If you'd like to contribute to this project, you can fork the repository and submit a pull request. 

To set up a development environment, run:
```bash
git clone https://github.com/salva/py-pluralsingular.git
cd py-pluralsingular
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -e .
```

To run tests, you can use **pytest**:
```bash
pytest
```

---

## 📝 **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 **Contributing**
Corrections to the rules and exceptions are welcome! Contributions, support for other language backends, and any feedback or suggestions are highly appreciated. If you find any incorrect behavior or have suggestions for improvement, please submit an issue or a pull request.

---

## 🔗 **Links**
- **GitHub**: [https://github.com/salva/py-pluralsingular](https://github.com/salva/py-pluralsingular)
- **Author**: Salvador Fandiño (sfandino@yahoo.com)

