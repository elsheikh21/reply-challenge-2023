import logging
import os
from typing import List, Tuple
import fnmatch

from kenken_solver.csp import backtracking_search
from kenken_solver.kenken import Kenken, parse


def parse_file(_path: str) -> List[str]:
    with open(_path, mode="r") as csvfile:
        _data = list(csvfile)
    return _data


def split_txt_file(_data: List[str]) -> Tuple[List[List[str]], List[str]]:
    _sudoku_matrix = [d.strip().split() for d in _data[:5]]
    _sudoku_instructions = [d.strip() for d in _data[6:]]
    return _sudoku_matrix, _sudoku_instructions


def create_example(_sudoku_matrix: List[List[str]], _sumdoku_intrx: List[str]) -> str:
    matrix_positional = {}
    for i in range(len(_sudoku_matrix)):
        sudoku_matrix_row = _sudoku_matrix[i]
        for j in range(len(sudoku_matrix_row)):
            char = sudoku_matrix_row[j]
            position = (j + 1, i + 1)
            if char in matrix_positional:
                matrix_positional[char] += (position,)
            else:
                matrix_positional[char] = (position,)

    matrix = {}
    for char_oper_op in _sumdoku_intrx:
        char, result, operator = char_oper_op.split()
        matrix[char] = f"({matrix_positional[char]}, '{operator}', {result})\n"

    _example = f"{len(_sudoku_matrix)}\n"
    for char in matrix:
        _example += matrix[char]
    return _example


def solve_killer_sudoku(_path: str) -> str:
    data = parse_file(_path)

    sudoku_matrix, sudoku_instructions = split_txt_file(data)
    logging.info(f"The input sequence is: \n  {sudoku_matrix}")
    logging.info(f"The input is: \n  {sudoku_instructions}")

    example = create_example(sudoku_matrix, sudoku_instructions)
    logging.debug(f"The example created is:  \n{example}")

    size, cliques = parse(example)
    logging.debug(
        f"From example we can deduce: \n- size is '{size}'\n- Cliques are:\n {cliques}"
    )

    logging.info("Solving the example")

    ken = Kenken(size, cliques)
    assignment = backtracking_search(ken)
    res = ken.display(assignment, return_res=True)
    logging.info(f"Killer Sudoku is solved!, The answer is '{res}'")
    return res


def fetch_files_with_pattern(root_dir: str, pattern: str) -> List[str]:
    # Initialize an empty list to store the matching file paths
    matching_files = []

    # Walk through the directory tree and find matching files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in fnmatch.filter(filenames, pattern):
            # Get the full path to the matching file
            file_path = os.path.join(dirpath, filename)
            matching_files.append(file_path)
    return matching_files


def unzip_file(zip_file_path, password):
    import py7zr
    with py7zr.SevenZipFile(zip_file_path, 'r', password=password) as archive:
        archive.extractall(path="/tmp")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    root_directory = os.getcwd()
    files_names = fetch_files_with_pattern(root_dir=root_directory, pattern='lvl_*.zip')

    path = os.path.join(os.getcwd(), "lvl_1.txt")
    prev_puzzle_result = solve_killer_sudoku(path)

    # zip_file_path = files_names[-1]
    # unzip_file(zip_file_path, prev_puzzle_result)
