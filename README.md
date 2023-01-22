# Pythra - Multi-language Python Translator

## Introduction:

Pythra is designed to translate python keywords in any language to their English equivalent. This can be useful for programmers who are learning a new language or are working with code written in a different language. The program uses a dictionary of keywords and their translations, and will output the English equivalent of any python keyword inputted.

---

<br>

> **Note:** The program currently only supports a limited number of languages and keywords, and may not accurately translate all input. It is recommended to double check the translation with a reliable source before using in production code.

<br>

### Requirements:

- Install [Python 3.10](https://www.python.org/) which includes [Pip](https://pypi.org/project/pip/)
- Its only dependency is [Typer 0.7.0](https://typer.tiangolo.com/)

<br>

### Installation using pyproject.toml:

Change directory to the source code, then run this in your CLI:

```
$ pip install .
```

<br>

### Usage:

To use the Pythra, simply run the pythra or python script using the `pythra` keyword. The program will then translate scripts' keywords into Python's English equivalent and compile them as Python files inside the compiled directory. If no provided file argument, Pythra will only compile the scripts without executing any script. You can use either _".puta"_, _".py"_ or specific language extension to run your script.

```bash
$ pythra [OPTIONS] [FILE_PATH]
```

| Arguments | Description               | Default | Optional |
| --------- | ------------------------- | ------- | -------- |
| file_path | File path of pythra file. | None    | Yes      |

<br>

| Options              | Description                                                                      |
| -------------------- | -------------------------------------------------------------------------------- |
| --version, -v        | Display the current version of pythra.                                           |
| --language, -l       | Override the foreign language.                                                   |
| --no-run             | Force not to run the script.                                                     |
| --install-completion | Install completion for the current shell.                                        |
| --show-completion    | Show completion for the current shell, to copy it or customize the installation. |
| --help               | Show this message and exit.                                                      |

<br>

### Example:

Project structure

> It is optional to have *\_\_pythraconfig\_\_.json* to compile and run the Pythra file, but it is recommended to have it in your directory to organize your Pythra project.

```
myproject/
    README.md
    LICENSE.md
    myproject/
		__pythraconfig__.json
		module.puta
		package_1/
			package/
				module.puta
			module_1.puta
			module_2.puta
		package_2/
			module.puta
```

<br>

The default foreign language of Pythra is _Tagalog_. If you did not put a Pythra configuration in your project, Pythra will compile your script in _Tagalog_. These are the following properties of `__pythraconfig__.json` and its default value:

```jsonc
{
  "rootDir": ".",                  // The directory where the compiler starts to find the pythra script.
  "compiledDir": "__compiled__",   // The directory where the compiled python script stored.
  "language": "tagalog",           // Foreign language of pythra script.
  "runOnCompile": "true"           // If true, pythra will execute the translated python script.
}
```

<br>

**TAGALOG:**

Create a file `kumusta_mundo.ptg` with the following tagalog script.

```python
dep kumustaMundo():
	mag_print("Kumusta mundo!")

kumustaMundo()
```

Run the file in CLI using the command:

```bash
$ pythra kumusta_mundo.ptg

# Output: Kumusta mundo!
```

<br>

**SPANISH:**

Create a file `hola_mundo.puta` with the following spanish script

```python
def holaMundo():
	imprimo("Hola, mundo!")

holaMundo()
```

Run the file in CLI using the command:

```bash
$ pythra -l spanish hola_mundo.puta

# Output: Hola, mundo!
```

<br>

### Pythra without argument

It will just compile all the files under the current directory if you execute the `pythra` keyword without the argument or the _"runOnCompile"_ property of the `__pythraconfig__.json` is set to false. By default _"runOnCompile"_ is set to true.

```bash
$ pythra
```

---

<br>

## Supported Languages

| Language | Specific File Extension |                                             |
| -------- | ----------------------- | ------------------------------------------- |
| Tagalog  | _.ptg_                  | [Documentation](./documentation/tagalog.md) |
| Spanish  | _.pes_                  | [Documentaion](./documentation/spanish.md)  |

---

<br>

## Conclusion:

This program provides a quick and easy way for programmers to translate python keywords in different languages to their English equivalent. It can save time and effort when working with code written in a foreign language. However, it should be used with caution and double-checked with a reliable source before being used in production code.
