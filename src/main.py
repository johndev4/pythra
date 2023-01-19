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
        "", "-l", "--language", help="Override the foreign language.")
):
    if version is True:
        display_version()
    else:
        try:
            if lang_name is not None and lang_name != "":
                __compiler = Compiler(language=Language(lang_name))
            else:
                __compiler = Compiler(language=Language())

            __compiler.compile(file_path)

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
