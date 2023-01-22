import json
import os
import re
import pkg_resources


class AppUtil:
    def __init__(self):
        self.__appdir = os.path.realpath(os.path.dirname(__file__))
        self.__currentdir = os.getcwd()
        self.__pkg_distribution = pkg_resources.get_distribution("pythra")

    def get_pythra_config(self):
        default_config_path = os.path.join(
            self.__appdir, "constants", "pythra-config.default.jsonc")

        if os.path.exists(default_config_path):
            default_config_data = dict(self.parse_jsonc(default_config_path))
            default_root_dir = os.path.abspath(
                default_config_data["rootDir"])
            default_extensions = map(
                lambda ext: f".{str(ext).replace('.', '')}", default_config_data['defaultExtensions'])

            # Build default config dictionary
            default_config_dict = {
                "default_extensions": default_extensions,
                "root_dir": default_root_dir,
                "compiled_dir": default_config_data["compiledDir"],
                "language": default_config_data["language"],
                "run_on_compile": default_config_data["runOnCompile"]
            }
        else:
            return None

        # Find __pythraconfig__.jsonc file starting from current directory up to
        # the root of the computer file system
        custom_config_path = self.find_file("__pythraconfig__.jsonc")

        # If __pythraconfig__.jsonc file not found, try to find
        # __pythraconfig__.json file starting from current directory up to the
        # root of the computer file system
        if custom_config_path == None:
            custom_config_path = self.find_file("__pythraconfig__.json")

        if custom_config_path != None:
            custom_config_data = dict(self.parse_jsonc(custom_config_path))
            custom_root_dir = self.build_root_directory(
                custom_config_data["rootDir"], custom_config_path)

            # Build custom config dictionary
            custom_config_dict = {
                **default_config_dict,
                "root_dir": custom_root_dir if custom_root_dir else default_config_dict["root_dir"],
                "compiled_dir": custom_config_data.get("compiledDir", default_config_dict["compiled_dir"]),
                "language": custom_config_data.get("language", default_config_dict["language"]),
                "run_on_compile": custom_config_data["runOnCompile"]
            }

            return custom_config_dict
        else:
            # Return the default config dictionary if the __pythraconfig__.jsonc
            # not found
            return default_config_dict

    def find_file(self, file_to_find):
        splitted_current_directory = self.__currentdir.split("\\")
        splitted_cd_len = len(splitted_current_directory)

        for i in range(splitted_cd_len):
            current_directory = "\\".join(
                splitted_current_directory[0:splitted_cd_len - i])

            for file in os.scandir(current_directory):
                filename = os.path.basename(file)

                if file.is_file() and filename == file_to_find:
                    return os.path.abspath(file)

        else:
            return None

    def build_root_directory(self, root: str, config_path: str):
        dirname = os.path.dirname(config_path)
        root_dir = os.path.abspath(os.path.join(dirname, root))
        return root_dir

    def get_app_version(self):
        return self.__pkg_distribution.version

    def get_current_dir(self):
        return self.__currentdir

    def get_app_dir(self):
        return self.__appdir

    def split_filename(self, file: str):
        splitted_file_path = file.split("\\")
        splitted_file_path.reverse()
        return os.path.splitext(splitted_file_path[0])

    def get_supported_languages(self) -> set:
        lang_models = os.path.join(self.__appdir, "language_models")
        subdirs = os.listdir(lang_models)
        if (subdirs):
            return set(subdirs)
        else:
            return set()

    def parse_jsonc(self, file_path: str):
        """
        Parse a JSONC file and return the parsed JSON data.

        Parameters: file_path:str - path to jsonc file
        """

        # Regular expression to match single-line comments
        single_line_regex = re.compile(r'//.*')
        # Regular expression to match multi-line comments
        multi_line_regex = re.compile(r'/\*.*?\*/', re.DOTALL)

        with open(file_path, 'r') as jsonc_file:
            jsonc_string = jsonc_file.read()

        # Remove single-line comments and multi-line comments
        jsonc_string = single_line_regex.sub('', jsonc_string)
        jsonc_string = multi_line_regex.sub('', jsonc_string)

        return json.loads(jsonc_string)
