

import sys

import read_file
import simplex_first_phase
import simplex_second_phase


def __simplex(file_name):

	tableau,A = read_file.file_to_tableau(file_name)

	tableau = simplex_first_phase.solve(tableau,A)

	simplex_second_phase.solve(tableau)

if __name__ == "__main__":
    __simplex(sys.argv[1])
