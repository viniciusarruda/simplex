# -*- coding: utf-8 -*-


class Tableau:

    def __init__(self, file_name):
        self.tableau = None
        self.I = None
        self.J = None
        self.A = None
        self.option = None
        self.tableau_n = 0

        self.__load_tableau_from_file(file_name)


    def show(self, out=None, inn=None, answer=None, custom=None):

        if answer is not None:
            tableau_info = "Tableau Final: " + answer
            final_space = "\n\n"
        elif custom is not None:
            tableau_info = "Tableau {}: ".format(self.tableau_n) + custom
            self.tableau_n += 1
            final_space = ""
        else:
            tableau_info = "Tableau {}: Vai entrar x{} e sair x{}".format(self.tableau_n, inn, self.I[out - self.option])
            self.tableau_n += 1
            final_space = ""

        print "\n\n" + tableau_info + "\n" + self.__str__() + final_space


    def __str__(self):

        header = ['z'] + ['x' + str(i) for i in self.I]
        sets = "I: " + str(self.I) + "     J: " + str(self.J)
        z = 'z* = ' + '{0:.3f}'.format(self.tableau[self.option - 1][0])

        if self.option == 2:
            header = ['za'] + header
            sets += "     A: " + str(self.A)
            z = 'za* = ' + '{0:.3f}'.format(self.tableau[0][0]) + "\n" + z

        solution = [0.0] * (len(self.tableau[0]) - 1)
        for i in xrange(0, len(self.I)):
            solution[self.I[i] - 1] = self.tableau[i + self.option][0]

        tmp = [['', 'b'] + ['x' + str(x) for x in xrange(1, len(self.tableau[0]))]]
        tmp += [[header[i]] + ['{0:.3f}'.format(x) for x in self.tableau[i]] for i in xrange(0, len(self.tableau))]

        shift = max([len(e) for row in tmp for e in row])

        separator = '+' + '+'.join(['~' * shift for _ in xrange(0, len(self.tableau[0]) + 1)]) + '+'

        return separator + "\n" + \
               ''.join(['|' + '|'.join('{0:>{shift}}'.format(x, shift=shift) for x in row) + '|\n' for row in tmp]) + \
               separator + \
               "\n" + sets + "\n" + z + '\nx* = (' + ', '.join(['{0:.3f}'.format(s) for s in solution]) + ')'


    def __load_tableau_from_file(self, file_name):

        not_in_format_msg = "The file is not in the correct format or the LPP is not in the standard form."

        with open(file_name, 'r') as file:
            self.option = int(file.readline().replace('\n', ''))

            if self.option != 1 and self.option != 2:
                raise ValueError(not_in_format_msg)

            rows,cols = map(int, file.readline().replace('\n','').split())

            m = rows - self.option

            self.tableau = [map(float, file.readline().replace('\n','').split()) for _ in xrange(0, rows)]

            # ld na primeira coluna
            for i in xrange(0, rows):
                self.tableau[i] = [self.tableau[i][-1]] + self.tableau[i][0:-1]


            # lista em ordem das variaveis basicas
            self.I = []
            for j in xrange(0, cols):
                n_zeros = 0
                n_ones = 0

                jj = j
                for i in xrange(self.option - 1, rows):

                    if self.tableau[i][j] == 1.0:
                        n_ones += 1
                        ii = i
                    elif self.tableau[i][j] == 0.0:
                        n_zeros += 1
                    else:
                        break

                if n_ones == 1 and n_zeros == m:
                    self.I.append((ii, jj))


            if len(self.I) != m:
                raise ValueError(not_in_format_msg)

            self.I.sort(key=lambda tup: tup[0])
            self.I = list(zip(*self.I)[1])
            self.J = [j for j in xrange(1, cols) if j not in self.I]  # except 1 because is LD


            self.tableau[0] = [-x for x in self.tableau[0]]  # invertendo o sinal


            if self.option == 2:

                self.tableau[1] = [-x for x in self.tableau[1]]  # invertendo o sinal

                self.A = [j for j in self.I if self.tableau[0][j] == -1.0]

                if len(self.A) < 1 or len(self.A) > m:
                    raise ValueError(not_in_format_msg)


                # colocando a artificial na base efetivamente
                self.show(custom="Vai zerar os valores das variáveis artificiais de za")

                artificial_in_base = [i + 2 for i in xrange(0, len(self.I)) if self.I[i] in self.A]

                for i in artificial_in_base:
                    self.tableau[0] = [a + b for a, b in zip(self.tableau[0], self.tableau[i])]


    def change_base(self, i, j):

        div = self.tableau[i][j]
        self.tableau[i] = map(lambda x: x / div, self.tableau[i])

        tmp_range = range(0, len(self.tableau))
        tmp_range.remove(i)

        for ii in tmp_range:
            b = -self.tableau[ii][j]
            tmp = map(lambda x: x * b, self.tableau[i])
            self.tableau[ii] = map(lambda a: sum(a), zip(tmp, self.tableau[ii]))

        self.__adjust_JI(i,j)

    def __adjust_JI(self, i, j):

        tmp = self.I[i - self.option]
        self.I[i - self.option] = j
        self.J.remove(j)
        self.J.append(tmp)
        self.J.sort()


    def remove_artificial(self):

        for a in self.A:
            if a in self.J:  # if not in, é porque tem variável artificial na base e o processo abaixo irá retirar
                self.J.remove(a)

        l = [(index + 2, i) for index, i in enumerate(self.I) if i in self.A]  # se tem basica artificial

        for i, a in l:
            for j in xrange(0, len(self.J)):
                if self.tableau[i][self.J[j]] != 0.0:
                    self.show(i, self.J[j])
                    self.change_base(i, self.J[j])
                    self.J.remove(a)  # this should keep the order !
                    break

        self.show(custom="Vai remover a coluna das variáveis artificiais e a linha za")

        l = [(index + 2, i) for index, i in enumerate(self.I) if i in self.A]  # checa se ainda tem basica artificial

        if l != []: # remover na forca pois esta tudo nulo !!! só pensar que vai ver que está !
            self.tableau = [self.tableau[i] for i in xrange(0, len(self.tableau)) if i not in zip(*l)[0]]
            for i in zip(*l)[1]:
                self.I.remove(i)

        # old function truncate_tableau(self):
        self.tableau = [[row[0]] + [row[j] for j in xrange(1, len(row)) if j not in self.A] for row in self.tableau[1:]]
        self.option = 1


    def get_pivot(self):

        j = max(map(lambda j: (j, self.tableau[0][j]), self.J), key=lambda x: x[1])[0]
        l = [i for i in range(self.option, len(self.tableau)) if self.tableau[i][j] > 0.0]
        l = [(self.tableau[i][0] / self.tableau[i][j], i) for i in l]
        i = min(l, key=lambda div: div[0])[1]
        self.show(i, j)
        return i, j

    def is_degenerate(self):

        for row in self.tableau[1:]: # 1: only runs in option 1
            if row[0] == 0.0:
                return True
        return False

    def has_multiple_solutions(self):
        return max([self.tableau[0][j] for j in self.J]) == 0.0

    def is_M_empty(self):
        return self.tableau[0][0] != 0.0

    def is_solution(self):
        return max([self.tableau[0][j] for j in self.J]) <= 0.0

    def goes_to_minus_inf(self):

        for j in self.J:
            inf = True
            if self.tableau[0][j] > 0.0:  # apenas se for candidata a entrar na base !
                for row in self.tableau[1:]: # just checked in option 1 (second phase)
                    if row[j] > 0.0:
                        inf = False
                        break
                if inf is True:  # -infinito
                    return True
        return False
