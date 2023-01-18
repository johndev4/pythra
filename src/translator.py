from language import Language


class Translator:

    def __init__(self):
        self.language = Language()

    def translate(self, code: str):
        splitters = set(self.language.get("splitters"))
        keywords = self.language.get("keywords")
        tokens = []
        current_token = ""
        quotations = {"\"", "\'"}
        curly_brackets = {"{", "}"}
        inside_quotations = False
        inside_curly_brackets = False
        period_on = False

        for character in code:
            if character in splitters:
                if character in quotations:
                    inside_quotations = not inside_quotations
                elif character in curly_brackets:
                    inside_curly_brackets = not inside_curly_brackets
                elif character == ".":
                    if current_token in keywords and (inside_quotations == False or inside_curly_brackets == True):
                        current_token = keywords[current_token]
                    period_on = True
                elif current_token in keywords and (inside_quotations == False or inside_curly_brackets == True):
                    if period_on == False:
                        current_token = keywords[current_token]
                    else:
                        period_on = False

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
