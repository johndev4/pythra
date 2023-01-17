# Pythra - Multi-language Python Translator

## Introduction:

Pythra is designed to translate python keywords in any language to their English equivalent. This can be useful for programmers who are learning a new language or are working with code written in a different language. The program uses a dictionary of keywords and their translations, and will output the English equivalent of any python keyword inputted.

---

<br>

> **Note:** The program currently only supports a limited number of languages and keywords, and may not accurately translate all input. It is recommended to double check the translation with a reliable source before using in production code.

<br>

### Prerequisites:

- Install [Python 3.10](https://www.python.org/) which includes [Pip](https://pypi.org/project/pip/)

<br>

### Installation using pyproject.toml:

- Change directory to the source code, then run this in your CLI:

```
pip install --editable .
```

<br>

### Usage:

To use the Pythra, simply run the pythra or python script using the `pythra` keyword. The program will then translate scripts' keywords into Python's English equivalent and compile them as Python files inside the compiled directory. If no provided file argument, Pythra will only compile the scripts without executing any script. You can use either _".puta"_, _".py"_ or specific language extension to run your script.

```bash
pythra [OPTIONS] [FILE_PATH]
```

| Arguments | Description               | Default |
| --------- | ------------------------- | ------- |
| file_path | File path of pythra file. | None    |

<br>

| Options              | Description                                                                      |
| -------------------- | -------------------------------------------------------------------------------- |
| --version, -v        | Display the current version of pythra.                                           |
| --install-completion | Install completion for the current shell.                                        |
| --show-completion    | Show completion for the current shell, to copy it or customize the installation. |
| --help               | Show this message and exit.                                                      |

<br>

### Example:

Project structure

> It is optional to have *\_\_pythraconfig\_\_.json* to compile and run the pythra file, but it is recommended to have it in your directory to organize your pythra project.

```
proyekto/
    README.md
    LISYENSYA.md
    proyekto/
		__pythraconfig__.json
		modulo.puta
		kaha_1/
			kaha/
				modulo.puta
			modulo_1.puta
			modulo_2.puta
		kaha_2/
			modulo.puta
```

Filename: _\_\_pythraconfig\_\_.json_

```json
{
  "rootDir": ".",
  "compiledDir": "__compiled__",
  "language": "tagalog",
  "runOnCompile": "true"
}
```

Filename: _kumusta_mundo.ptg_

```python
dep kumustaMundo():
	mag_print("Kumusta mundo!")

kumustaMundo()
```

CLI

```bash
pythra kumusta_mundo.ptg
```

<small>Output:</small>

```
Kumusta mundo!
```

---

<br>

## Supported Languages

| Language | Specific File Extension |
| -------- | ----------------------- |
| Tagalog  | _.ptg_                  |
| Spanish  | _.pes_                  |

---

<br>

## Conclusion:

This program provides a quick and easy way for programmers to translate python keywords in different languages to their English equivalent. It can save time and effort when working with code written in a foreign language. However, it should be used with caution and double-checked with a reliable source before being used in production code.