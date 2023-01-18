from language import Language


language = Language()


def __translate(code: str):
    splitters = set(language.get("splitters"))
    keywords = language.get("keywords")
    tokens = []
    current_token = ""
    quotations = {"\"", "\'"}
    curly_brackets = {"{", "}"}
    inside_quotations = False
    inside_curly_brackets = False
    period_on = False

    for c in code:
        if c in splitters:
            if c in quotations:
                inside_quotations = not inside_quotations
            elif c in curly_brackets:
                inside_curly_brackets = not inside_curly_brackets
            elif current_token in keywords and (inside_quotations == False or inside_curly_brackets == True):
                if period_on == False:
                    current_token = keywords[current_token]
                
            if c == ".":
                period_on = True
            else:
                period_on = False

            tokens.append(current_token)
            tokens.append(c)
            current_token = ""
        else:
            current_token += c

    if current_token in keywords and inside_quotations == False:
        current_token = keywords[current_token]
    tokens.append(current_token)
    translated_code = "".join(tokens)

    return translated_code


# Test Case:
code = "\nmula_sa kaha.mag_print mag_import kumustaMundo"
expected_output = "\nfrom kaha.mag_print import kumustaMundo"
print(f'Output: {__translate(code)}\n\n')
assert __translate(code) == expected_output

code = "\nmula_sa kaha.tao mag_import Tao"
expected_output = "\nfrom kaha.tao import Tao"
print(f'Output: {__translate(code)}\n\n')
assert __translate(code) == expected_output

code = "sarili.mag_print()"
expected_output = "self.mag_print()"
print(f'Output: {__translate(code)}\n\n')
assert __translate(code) == expected_output

code = "f'{sarili.x}'"
expected_output = "f'{self.x}'"
print(f'Output: {__translate(code)}\n\n')
assert __translate(code) == expected_output

code = "{sarili.x}"
expected_output = "{self.x}"
print(f'Output: {__translate(code)}\n\n')
assert __translate(code) == expected_output

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
