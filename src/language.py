import os
import json

from util import AppUtil


class Language:

    def __init__(self):
        self.__util = AppUtil()
        app_dir = self.__util.get_app_dir()
        self.__lang_dir = os.path.join(app_dir, "language_models")
        self.__const_dir = os.path.join(app_dir, "constants")
        lang = self.__get_lang_from_config()

        with open(os.path.join(self.__lang_dir, lang, "data.json"), "r") as f_lang, \
                open(os.path.join(self.__const_dir, "splitters.json"), "r") as f_splitters:
            lang_data = json.load(f_lang)
            splitters_data = json.load(f_splitters)
            self.__lang = {
                "name": lang,
                "keywords": lang_data["keywords"],
                "splitters": splitters_data["SPLITTERS"]
            }

    def __get_lang_from_config(self):
        config = self.__util.get_pythra_config()
        lang = config["language"]
        supported_languages = self.get_list()
        if lang != None and lang in supported_languages:
            return lang
        else:
            raise Exception("Language does not exist.")

    def get(self, key: str):
        if key != None:
            return self.__lang[key]
        else:
            return self.__lang

    def get_list(self):
        subdirs = os.listdir(self.__lang_dir)
        if (subdirs):
            return subdirs
        else:
            return []

    # def exists(self, lang: str):
    #     if len(self.get_list()) > 0:
    #         return (lang in self.get_list())
    #     return False

    def get_lang_ext(self) -> str:
        with open(os.path.join(self.__const_dir, "language-extension-mapping.json"), "r") as f_lang_ext_mapping:
            data = json.load(f_lang_ext_mapping)
            language_name = self.get("name")
            return f".{str(data[language_name]).replace('.', '')}"
