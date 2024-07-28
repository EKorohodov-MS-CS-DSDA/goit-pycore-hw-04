import re
from pathlib import Path

KEYS = ["id", "name", "age"]

def get_cats_info(path: str) -> list[dict]:
    """
    A function to get information about cats from a file given its path.
    Parameters:
        path (str): The path to the file containing cat information.
    Returns:
        list[dict]: A list of dictionaries containing the parsed cat information with keys 
            'id', 'name', and 'age'.
    """
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.rstrip() for line in f.readlines()]
            if len(lines) == 0:
                raise ValueError(f"File {path} is empty.")

        return [parse_cat_info(line) for line in lines]

    except FileNotFoundError:
        print(f"File {path} not found.")
    except ValueError as e:
        print(f"Error: {e}")
    return []


def parse_cat_info(line: str) -> dict:
    """
    A function to parse the information of a cat record from the given line.
    Parameters:
        line (str): A string containing the cat record to be parsed.
    Returns:
        dict: A dictionary containing the parsed cat information with keys 'id', 'name', and 'age'.
    """
    pattern = r"(\w+)"
    match = re.findall(pattern, line)

    if len(match) != 3:
        raise ValueError(f"Invalid record: {match}")

    return {KEYS[i]: match[i] for i in range(len(match))}


def main():
    print(get_cats_info("Task2_data.txt"))

if __name__ == "__main__":
    main()
