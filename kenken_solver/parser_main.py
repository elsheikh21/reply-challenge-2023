import csv
import os
from typing import List, Tuple


def parse_file(_path: str) -> List[str]:
    with open(_path, "r") as csvfile:
        _data = list(csvfile)
    return _data


def split_txt_file(data: List[str]) -> Tuple[List[str], List[str]]:
    sudoku_matrix = [d.strip().split() for d in data[:5]]
    sumdoku_intrx = [d.strip() for d in data[6:]]
    return sudoku_matrix, sumdoku_intrx


def create_example(_sudoku_matrix: List[str], _sumdoku_intrx: List[str]) -> str:
    matrix_positional = {}
    for i in range(len(_sudoku_matrix)):
        sudoku_matrix_row = _sudoku_matrix[i]
        for j in range(len(sudoku_matrix_row)):
            char = sudoku_matrix_row[j]
            if char in matrix_positional:
                matrix_positional[char] += ((i, j),)
            else:
                matrix_positional[char] = ((i, j),)

    matrix = {}
    for char_oper_op in _sumdoku_intrx:
        char, result, operator = char_oper_op.split()
        matrix[char] = f"({matrix_positional[char]}, '{operator}', {result})\n"

    example = f"{len(matrix)}\n"
    for char in matrix:
        example += matrix[char]
    return example


if __name__ == "__main__":
    path = os.path.join(os.getcwd(), "lvl_1.txt")
    data = parse_file(path)

    sudoku_matrix, sumdoku_intrx = split_txt_file(data)
    print(
        f"The input sequence is: {sudoku_matrix} \n",
        f"The input is: {sumdoku_intrx} \n",
    )

    example = create_example(sudoku_matrix, sumdoku_intrx)
    print(f"The example created is:  \n{example} \n")
