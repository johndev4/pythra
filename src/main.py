import os
import shutil
import subprocess
from language import Language
from translator import Translator
import typer
from util import AppUtil


app = typer.Typer()
__util = AppUtil()
__language = Language()
__translator = Translator()

pythra_config = __util.get_pythra_config()
current_dir = __util.get_current_dir()
root_dir = pythra_config['root_dir']
compiled_dir = f"{root_dir}\\{pythra_config['compiled_dir']}"
lang_ext = __language.get_lang_ext()
file_extensions = set([*pythra_config['default_extensions'], lang_ext])
splitted_root_dir = str(root_dir).split('\\')
root_name = splitted_root_dir[-1]


@app.command(help="Interpret and compile all none english python file then execute the main file or given file.")
def pythra(
    file_path: str = typer.Argument(None, help="File path of pythra file."),
    version: bool = typer.Option(
        False, "-v", "--version", help="Display the current version of pythra.")
):
    if version is True:
        display_version()
    else:
        compile(file_path)


def compile(file_path: str = None):
    if file_path is not None:
        # Build the packages and run the provided file
        filename, file_ext = __util.split_filename(file_path)

        if file_ext in file_extensions:
            to_run_python_path = build_packages()
            if bool(pythra_config["run_on_compile"]) is True:
                to_run_python_file = os.path.join(
                    to_run_python_path, f"{filename}{file_ext}").replace(f"{file_ext}", ".py")
                subprocess.run(["python", f"{to_run_python_file}"])
        else:
            raise Exception("Incorrect file extension. Must be \"" +
                            "\", \"".join(file_extensions) + "\"")
    else:
        # Build only the packages
        build_packages()


def display_version():
    """
    Prints the version of Pythra.
    """
    typer.echo(f"Pythra v{__util.get_app_version()}")


def interpret(file_path: str):
    _, file_ext = __util.split_filename(file_path)

    if file_ext in file_extensions:
        with open(file_path, "r") as f:
            code = f.read()

        pycode = __translator.translate(code)
        py_filename = file_path.replace(
            root_dir, f"{compiled_dir}\\{root_name}").replace(f"{file_ext}", ".py")

        with open(f"{py_filename}", "w") as python_file:
            python_file.write(pycode)
    else:
        raise Exception("Incorrect file extension. Must be \"" +
                        "\", \"".join(file_extensions) + "\"")


def build_packages():
    to_run_python_path = None

    if os.path.exists(compiled_dir):
        shutil.rmtree(compiled_dir)

    for dirpath, _, filenames in os.walk(root_dir):
        if dirpath == compiled_dir:
            continue

        new_directory = str(dirpath).replace(
            root_dir, f"{compiled_dir}\\{root_name}")
        os.makedirs(new_directory)
        open(f"{new_directory}\\__init__.py", "w").close()

        for file in set(filenames):
            _, file_ext = os.path.splitext(file)

            if file_ext in file_extensions:
                if current_dir == dirpath:
                    to_run_python_path = new_directory
                interpret(f"{dirpath}\\{file}")
            else:
                continue

    return to_run_python_path


def initApp():
    app()


# if __name__ == "__main__":
#     app()
