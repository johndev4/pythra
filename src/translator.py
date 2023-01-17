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
