import json
import os
from compiler import Compiler
from language import Language
import typer
from util import AppUtil
# from rich import print


app = typer.Typer()
__util = AppUtil()


@app.command(help="Interpret and compile all none english python file then execute the main file or given file.")
def pythra(
    file_path: str = typer.Argument(None, help="File path of pythra file."),
    version: bool = typer.Option(
        False, "-v", "--version", help="Display the current version of pythra."),
    lang_name: str = typer.Option(
        "", "-l", "--language", help="Override the foreign language."),
    no_run: bool = typer.Option(
        False, "--no-run", help="Force not to run the script.")
):
    if version is True:
        display_version()
    else:
        try:
            # Check if file extension exists in language mapping
            lang_provided_by_ext = None
            if file_path is not None:
                _, file_ext = __util.split_filename(file=file_path)
                app_dir = __util.get_app_dir()
                const_dir = os.path.join(app_dir, "constants")

                with open(os.path.join(const_dir, "language-extension-mapping.json"), "r") as f_lang_ext_mapping:
                    lang_ext_mapping = json.load(f_lang_ext_mapping)
                    for lang in lang_ext_mapping:
                        if lang_ext_mapping[lang] == file_ext:
                            # If exists, get the language name
                            lang_provided_by_ext = lang

            if lang_provided_by_ext is not None:
                __compiler = Compiler(language=Language(lang_provided_by_ext))
            elif lang_name is not None and lang_name != "":
                __compiler = Compiler(language=Language(lang_name))
            else:
                __compiler = Compiler(language=Language())

            __compiler.compile(file_path, no_run=no_run)

        except Exception as e:
            typer.echo(f'\nError: {e}\n\n')


def display_version():
    """
    Prints the version of Pythra.
    """
    version = __util.get_app_version()
    typer.echo(f"Pythra v{version}")


def initApp():
    app()


# if __name__ == "__main__":
#     app()
