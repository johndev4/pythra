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
