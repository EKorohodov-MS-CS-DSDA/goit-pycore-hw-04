def total_salary(path: str) -> tuple:
    """
    Calculate the total salary and average salary from a file containing employee records.
    Parameters:
        path (str): The path to the file containing employee records.
    Returns:
        tuple: A tuple containing the total salary and average salary. If the file is empty, 
            not found, or corrupted, a tuple of (0, 0) is returned.
    """
    try:
        total = 0
        average = 0

        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.rstrip() for line in f.readlines()]
            if len(lines) == 0:
                raise ValueError(f"File {path} is empty.")

        for line in lines:
            total += get_salary(line)

        average = total / len(lines)

        return total, average

    except FileNotFoundError:
        print(f"File {path} not found.")
    except ValueError as e:
        print(f"Error: {e}")

    # Exception case returns a tuple of (0, 0)
    return 0, 0


def get_salary(line: str) -> int:
    """
    A function to extract the salary value from a given line of employee record.
    Parameters:
        line (str): A string containing the employee's record.
    Returns:
        float: The extracted salary value from the record.
    Raises:
        ValueError: If the record does not contain a valid salary value.
    """
    record = line.split(",")
    if len(record) != 2 or not record[1].isdigit():
        raise ValueError(f"Invalid record: {record}")
    return float(record[1])


def main():
    try:
        total, average = total_salary("./HW/goit-pycore-hw-04/Task1_data.txt")
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
