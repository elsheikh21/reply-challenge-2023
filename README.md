# reply-challenge-2023

## Challenge 1

Solve killer Sudoku recursively and zip every nested zip file in order to get the flag.txt

They are 251 nested zip files each containing a password

### Dependencies

- to run the code
  - poetry shell
  - poetry run python parser-main.py # to create the example
- Other dependencies
  - `black` is used as a formatter
  - `isort` is used to organize imports

### Structure

the python file `parser-main.py` is responsible for converting the `txt` files into a format that `Kenken-solver` can use to solve the killer sudoku example given. The script is called via the file `run_sfida.sh` which is responsible for unzipping files using passwords found in every zip file
