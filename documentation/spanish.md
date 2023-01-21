# Pythra Documentation (Spanish)

---

## Data Types

_Text Type:_

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| texto           | str                        |

_Numeric Types:_

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| número          | int                        |
| floto           | float                      |
| complejo        | complex                    |

_Sequence Types:_

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| alcance         | range                      |
| lista           | list                       |
| tupla           | tuple                      |

_Mapping Type:_

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| diccionario     | dict                       |

_Set Types:_

| Spanish Keyword    | English Equivalent Keyword |
| ------------------ | -------------------------- |
| conjunto           | set                        |
| conjunto_congelado | frozenset                  |

_Boolean Type:_

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| booleano        | bool                       |

_Binary Types:_

| Spanish Keyword  | English Equivalent Keyword |
| ---------------- | -------------------------- |
| bytes            | bytes                      |
| bytesarray       | bytesarray                 |
| vista_de_memoria | memoryview                 |

_None Type:_

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| Ninguno         | None                       |

## Imports Keywords

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| desde           | from                       |
| importo         | import                     |

## Conditional Keywords

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| si              | if                         |
| más_si          | elif                       |
| más             | else                       |

## Loop Keywords

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| para            | for                        |
| mientras        | while                      |

## Try.. Except Keywords

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| intento         | try                        |
| excepto         | except                     |
| finalmente      | finally                    |

## Logical Operators

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| y               | and                        |
| o               | or                         |
| no              | not                        |

## Boolean Values

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| Cierto          | True                       |
| Falso           | False                      |

## Other Keywords

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| definición      | def                        |
| def             | [Short for depenisyon]     |
| clase           | class                      |
| mi              | self                       |

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| entro           | input                      |
| afirmo          | assert                     |
| ejecuto         | exec                       |
| imprimo         | print                      |
| con             | with                       |
| cedo            | yield                      |

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| vuelta          | return                     |
| pase            | pass                       |
| levanto         | raise                      |
| continúo        | continue                   |
| rompo           | break                      |

| Spanish Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| en              | in                         |
| como            | as                         |
| es              | is                         |

---

## Examples

Create a file `hola_mundo.pes` with the following tagalog script.

> You can use _.puta_, or _.py_ for the file extension.

```python
definición holaMundo():
	imprimo("Hola, mundo!")

holaMundo()
```

Run the file in CLI using the command:

```bash
pythra hola_mundo.pes
```

**_Output:_**

```
Hola, mundo!
```

### Conditional Example:

```python
tiempo = "la mañana"

si tiempo == "la mañana":
    imprimo("Buenos dias!") # Buenos dias!
más_si tiempo == "la tarde":
    imprimo("Buenas tardes!") # Buenas tardes!
más_si tiempo == "la noche":
    imprimo("Buenas noches!") #Buenas noches!
más:
    imprimo("Has entrado en el momento equivocado.") # Has entrado en el momento equivocado.
```

### Boolean Expression:

```python
es_cierto = Cierto # True
es_falso = Falso # False
```

### Try... and Exception

```python
intento:
    num_1 = mag_lagay("Enter a number: ")
    num_3 = num_1 + num_2

excepto Exception como e:
    imprimo(f'Eto ang error: {e}')
finalmente:
    imprimo("éxito!")
```
