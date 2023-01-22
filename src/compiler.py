import os
import shutil
import subprocess
from language import Language
from translator import Translator
from util import AppUtil


class Compiler:
    def __init__(self, language: Language) -> None:
        self.__util = AppUtil()
        self.__language = language
        self.__translator = Translator(language=self.__language)
        self.__pythra_config = self.__util.get_pythra_config()
        self.__root_dir = self.__pythra_config['root_dir']
        self.__compiled_dir = f"{self.__root_dir}\\{self.__pythra_config['compiled_dir']}"
        self.__current_dir = self.__util.get_current_dir()
        splitted_root_dir = str(self.__root_dir).split('\\')
        self.__root_name = splitted_root_dir[-1]
        lang_ext = self.__language.get_lang_ext()
        self.__file_extensions = set(
            [*self.__pythra_config['default_extensions'], lang_ext])

    def compile(self, file_path: str, **options):
        no_run = options.get('no_run', False)
        
        if file_path is not None:
            # Build the packages and run the provided file
            filename, file_ext = self.__util.split_filename(file_path)

            if file_ext in self.__file_extensions:
                to_run_python_path = self.build_packages()
                if bool(self.__pythra_config["run_on_compile"]) is True and no_run == False:
                    to_run_python_file = os.path.join(
                        to_run_python_path, f"{filename}{file_ext}").replace(f"{file_ext}", ".py")
                    subprocess.run(["python", f"{to_run_python_file}"])
            else:
                raise Exception("Incorrect file extension. Must be \"" +
                                "\", \"".join(self.__file_extensions) + "\"")
        else:
            # Build only the packages
            self.build_packages()

    def interpret(self, file_path: str):
        pass
        _, file_ext = self.__util.split_filename(file_path)

        if file_ext in self.__file_extensions:
            with open(file_path, "r") as f:
                code = f.read()

            pycode = self.__translator.translate(code)
            py_filename = file_path.replace(
                self.__root_dir, f"{self.__compiled_dir}\\{self.__root_name}").replace(f"{file_ext}", ".py")

            with open(f"{py_filename}", "w") as python_file:
                python_file.write(pycode)
        else:
            raise Exception("Incorrect file extension. Must be \"" +
                            "\", \"".join(self.__file_extensions) + "\"")

    def build_packages(self):
        to_run_python_path = None

        if os.path.exists(self.__compiled_dir):
            shutil.rmtree(self.__compiled_dir)

        for dirpath, _, filenames in os.walk(self.__root_dir):
            if dirpath == self.__compiled_dir:
                continue

            new_directory = str(dirpath).replace(
                self.__root_dir, f"{self.__compiled_dir}\\{self.__root_name}")
            os.makedirs(new_directory)
            open(f"{new_directory}\\__init__.py", "w").close()

            for file in set(filenames):
                _, file_ext = os.path.splitext(file)

                if file_ext in self.__file_extensions:
                    if self.__current_dir == dirpath:
                        to_run_python_path = new_directory
                    self.interpret(f"{dirpath}\\{file}")
                else:
                    continue

        return to_run_python_path
