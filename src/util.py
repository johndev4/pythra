import json
import os
import pkg_resources


class AppUtil:
    def __init__(self):
        self.__appdir = os.path.realpath(os.path.dirname(__file__))
        self.__currentdir = os.getcwd()
        self.__pkg_distribution = pkg_resources.get_distribution("pythra")

    def get_pythra_config(self):
        default_config_path = os.path.join(
            self.__appdir, "constants", "pythra-config.default.json")

        if os.path.exists(default_config_path):
            with open(default_config_path, "r") as fdefault_config:
                default_config_data = json.loads(fdefault_config.read())
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

        # Find __pythraconfig__.json file starting from current directory up to
        # the root of the computer file system
        custom_config_path = self.find_file("__pythraconfig__.json")

        if custom_config_path != None:
            with open(custom_config_path, "r") as fcustom_config:
                custom_config_data = dict(json.load(fcustom_config))
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
            # Return the default config dictionary if the __pythraconfig__.json
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
