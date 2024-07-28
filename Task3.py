from pathlib import Path
import sys
from colorama import Fore, Back, Style


def get_styled_string(element_name: str, element_type: str) -> None:
    """
    Get a styled string based on the element type.

    Parameters:
    element_name (str): The name of the element to be styled.
    element_type (str): The type of the element, either 'file' or 'directory'.

    Returns:
    str: The styled string based on the element type.
    """
    if element_type == "file":
        return Back.CYAN + Fore.WHITE + element_name + Style.RESET_ALL
    elif element_type == "directory":
        return Back.MAGENTA + Fore.WHITE + element_name + Style.RESET_ALL
    else:
        return element_name


def traverse_and_print_directory(path:Path, indent_level:int = 0, indent_char:str = "\t") -> None:
    """
    Recursively traverses a directory and prints its contents with indentation and styling.
    Parameters:
        path (Path): The path to the directory to traverse.
        indent_level (int, optional): The initial indentation level. Defaults to 0.
        indent_char (str, optional): The character used for indentation. Defaults to "\t".
    Returns:
        None: This function does not return anything.
    """
    for file in path.iterdir():
        if file.is_file():
            print(f"{indent_char * indent_level}{get_styled_string(file.name, 'file')}")
        elif file.is_dir():
            print(f"{indent_char * indent_level}{get_styled_string(file.name, 'directory')}")
            traverse_and_print_directory(file.absolute(), indent_level + 1, indent_char)


def print_directory_content(path: str) -> None:
    """
    Print the content of a directory.
    Parameters:
        path (str): The path to the target directory.
    """
    path_str = Path(path)
    try:
        if not path_str.exists():
            raise ValueError(f"Directory {path} not found.")
        elif not path_str.is_dir():
            raise ValueError(f"{path} is not a directory.")

        traverse_and_print_directory(path_str)

    except ValueError as e:
        print(f"Error: {e}")


def main():
    if len(sys.argv) > 1:
        print_directory_content(sys.argv[1])
    else:
        print(f"Usage: $python {sys.argv[0]} <directory>")

if __name__ == "__main__":
    main()
