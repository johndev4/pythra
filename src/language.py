import os
from src.util import AppUtil


class Language:

    def __init__(self, lang_name: str = None):
        self.__util = AppUtil()
        app_dir = self.__util.get_app_dir()
        self.__lang_dir = os.path.join(app_dir, "language_models")
        self.__const_dir = os.path.join(app_dir, "constants")
        lang = lang_name if lang_name is not None else self.__get_lang_from_config()
        self.__build_language(lang)

    def __build_language(self, lang_name: str):
        if lang_name in self.__util.get_supported_languages():
            lang_data = self.__util.parse_jsonc(
                os.path.join(self.__lang_dir, lang_name, "data.jsonc"))
            splitters_data = self.__util.parse_jsonc(
                os.path.join(self.__const_dir, "splitters.json"))
            lang_ext_mapping = self.__util.parse_jsonc(os.path.join(
                self.__const_dir, "language-extension-mapping.json"))

            self.__lang_dict = {
                "name": lang_name,
                "keywords": lang_data["keywords"],
                "splitters": splitters_data["SPLITTERS"],
                "file_extension": f".{str(lang_ext_mapping[lang_name]).replace('.', '')}"
            }
        else:
            raise Exception(
                f'"{lang_name}" is currently unsupported language.')

    def __get_lang_from_config(self):
        config = self.__util.get_pythra_config()
        lang = config["language"]
        supported_languages = self.__util.get_supported_languages()
        if lang != None and lang in supported_languages:
            return lang
        else:
            raise Exception("Language does not exist.")

    def get_dict(self, key: str):
        if key != None:
            return self.__lang_dict[key]
        else:
            return self.__lang_dict

    # def get_list(self):
    #     subdirs = os.listdir(self.__lang_dir)
    #     if (subdirs):
    #         return subdirs
    #     else:
    #         return []

    def get_lang_ext(self) -> str:
        return self.__lang_dict.get("file_extension", None)
