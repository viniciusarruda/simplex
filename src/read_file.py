

# Read file and return the tableau

# n: natural variables
# m: number of constraints

def file_to_tableau(file_name):

	n = None
	m = None
	tableau = None
	J = None

	#try:

	with open(file_name, 'r') as file:
		option = int(file.readline().replace('\n',''))

		if option != 1 and option != 2:
			raise

		rows,cols = map(int, file.readline().replace('\n','').split(" "))

		if option == 1:
			m = rows - 1
			n = cols - m - 1
		else:
			m = rows - 2
			n = cols - m - 1    # n aqui tem o numero de variaveis naturais mais o numero de variaveis artificiais


		tableau = []
		for i in xrange(0, rows):
			tableau.append(map(float, file.readline().replace('\n','').split(' ')))

		# ld na primeira coluna
		for i in xrange(0, rows):
			tableau[i] = [tableau[i][-1]] + tableau[i][0:-1]


		#lista em ordem das variaveis basicas
		I = []
		for col in xrange(0,cols):
			index = None
			count = 0.0
			for row in tableau[option:]:
				if row[col] == 1.0 or row[col] == 0.0:
					index = col
					count += row[col]
				else:
					count = 0.0
					break

			if count == 1.0:
				I.append(index + 1) # mais um do z za e tal

		if len(I) != m:
			raise # deve ser m mesmo !, a cada artificial colocada, eh devido ah uma de folga que ficou negativa

		if option == 1:
			A = None
		else:
			A = []
			for j in xrange(0, len(tableau[0])):
				if tableau[0][j] == 1.0:
					A.append(j+1)

			if len(A) < 1 or len(A) > m:
				raise

			for i in xrange(0, len(I)):
				for a in xrange(0, len(A)):
					if I[i] == A[a]:
						A[a] = (A[a], i+2)  # (indices de cima das artificiais, indice da lateral das artificiais)


		# invertendo o sinal
		if option == 1:
			tableau[0] = [-x for x in tableau[0]]
		else:
			tableau[0] = [-x for x in tableau[0]]
			tableau[1] = [-x for x in tableau[1]]


		if option == 1:
			tmp = ['Z'] + I
		else:
			tmp = ['Za','Z'] + I

		for i in xrange(0, rows):
			tableau[i].insert(0, tmp[i])

		# tableau.insert(0, range(2,cols+1))


	# except e:
	# 	print "The file is not in the correct format."
	# 	e.print()

	return tableau,A



