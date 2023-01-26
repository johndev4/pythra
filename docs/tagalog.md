# Pythra Documentation (Tagalog)

---

## Data Types

_Text Type:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| teksto          | str                        |

_Numeric Types:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| numero          | int                        |
| lutang          | float                      |
| kompleks        | complex                    |

_Sequence Types:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| saklaw          | range                      |
| lista           | list                       |
| tupla           | tuple                      |

_Mapping Type:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| diksyunaryo     | dict                       |

_Set Types:_

| Tagalog Keyword    | English Equivalent Keyword |
| ------------------ | -------------------------- |
| kumpol             | set                        |
| nakapirming_kumpol | frozenset                  |

_Boolean Type:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| bool            | bool                       |

_Binary Types:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| bytes           | bytes                      |
| bytesarray      | bytesarray                 |
| memoryview      | memoryview                 |

_None Type:_

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| Wala            | None                       |

## Imports Keywords

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| mula_sa         | from                       |
| mag_import      | import                     |

## Conditional Keywords

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| kung            | if                         |
| eh_paano_kung   | elif                       |
| kundi           | else                       |

## Loop Keywords

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| bawat           | for                        |
| habang          | while                      |

## Try.. Except Keywords

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| subukan         | try                        |
| maliban         | except                     |
| sa_wakas        | finally                    |

## Logical Operators

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| at              | and                        |
| o               | or                         |
| hindi           | not                        |

## Boolean Values

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| Totoo           | True                       |
| Mali            | False                      |

## Other Keywords

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| depenisyon      | def                        |
| dep             | [Short for depenisyon]     |
| klase           | class                      |
| sarili          | self                       |

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| mag_lagay       | input                      |
| igiit           | assert                     |
| isagawa         | exec                       |
| mag_print       | print                      |
| kalakip         | with                       |
| sumuko          | yield                      |

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| ibalik          | return                     |
| dumaan          | pass                       |
| itaas           | raise                      |
| ituloy          | continue                   |
| itigil          | break                      |

| Tagalog Keyword | English Equivalent Keyword |
| --------------- | -------------------------- |
| sa              | in                         |
| bilang          | as                         |
| ay              | is                         |

---

## Examples

Create a file `kumusta_mundo.ptg` with the following tagalog script.

> You can use _.puta_, or _.py_ for the file extension.

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

### Conditional Example:

```python
# note: pwedeng gumamit ng mag_lagay() at i-assign sa oras para kunin ang input ng user
oras = "Umaga"

kung oras == "Umaga":
    mag_print("Magandang umaga sa inyo!") # Magandang umaga sa inyo!
eh_paano_kung oras == "Tanghali":
    mag_print("Magandang tanghali sa inyo!") # Magandang tanghali sa inyo!
eh_paano_kung oras == "Gabi":
    mag_print("Magandang gabi sa inyo!") # Magandang gabi sa inyo!
kundi:
    mag_print("Mali ang oras na inilagay.") # Mali ang oras na inilagay.
```

### Boolean Expression:

```python
ay_totoo = Totoo # True
ay_mali = Mali # False
```

### Try... and Exception

```python
subukan:
    num_1 = mag_lagay("Enter a number: ")
    num_3 = num_1 + num_2

maliban Exception bilang e:
    mag_print(f'Eto ang error: {e}')
sa_wakas:
    mag_print('tagumpay!')
```
