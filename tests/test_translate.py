from language import Language


language = Language()


def __translate(code: str):
    splitters = set(language.get("splitters"))
    keywords = language.get("keywords")
    tokens = []
    current_token = ""
    quotations = {"\"", "\'"}
    brackets = {"{", "}"}
    inside_quotations = False
    inside_brackets = False
    for character in code:
        if character in splitters:
            if character in quotations:
                inside_quotations = not inside_quotations
            elif character in brackets:
                inside_brackets = not inside_brackets
            elif current_token in keywords and (inside_quotations == False or inside_brackets == True):
                current_token = keywords[current_token]

            tokens.append(current_token)
            tokens.append(character)
            current_token = ""
        else:
            current_token += character

    if current_token in keywords and inside_quotations == False:
        current_token = keywords[current_token]
    tokens.append(current_token)
    translated_code = "".join(tokens)

    return translated_code


# Test Case 1:
code = "dep suma(numero x, numero y): ibalik x + y"
expected_output = "def suma(int x, int y): return x + y"
# print(__translate(code))
assert __translate(code) == expected_output

# Test Case 2:
code = "kung x > y: mag_print('x is greater than y') kundi: mag_print('x is not greater than y')"
expected_output = "if x > y: print('x is greater than y') else: print('x is not greater than y')"
# print(__translate(code))
assert __translate(code) == expected_output

# Test Case 3:
code = "mula_sa math mag_import pi"
expected_output = "from math import pi"
# print(__translate(code))
assert __translate(code) == expected_output

# Test Case 4:
code = "Totoo x = Totoo"
expected_output = "True x = True"
# print(__translate(code))
assert __translate(code) == expected_output

# Test Case 5:
code = "kung Totoo: print('hello')"
expected_output = "if True: print('hello')"
assert __translate(code) == expected_output

# Test Case 6:
code = "dep add(a, b): return a + b"
expected_output = "def add(a, b): return a + b"
assert __translate(code) == expected_output

# Test Case 7 (Failed):
code = "print('kung Totoo')"
expected_output = "print('kung Totoo')"
# print(__translate(code))
assert __translate(code) == expected_output

# Test Case 8:
code = "kung Totoo:\n\tprint('hello')\n\tprint('world')"
expected_output = "if True:\n\tprint('hello')\n\tprint('world')"
assert __translate(code) == expected_output

# Test Case 9:
code = "# kung Totoo:\nprint('hello')"
expected_output = "# if True:\nprint('hello')"
assert __translate(code) == expected_output
