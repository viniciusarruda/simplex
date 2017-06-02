

import sys
from simplex import Simplex
from tableau import Tableau

if __name__ == "__main__":

    tableau = Tableau(sys.argv[1])
    simplex = Simplex(tableau)
    simplex.run()
