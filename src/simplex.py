

import sys

import read_file
import simplex_second_phase


def __simplex(file_name):

	n,m,tableau = read_file.file_to_tableau(file_name)

	simplex_second_phase.solve(tableau)


if __name__ == "__main__":
    __simplex(sys.argv[1])
