

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
			print "TO DO"
			return None
			m = rows - 2
			n = cols - m - 1    # n aqui tem o numero de variaveis naturais mais o numero de variaveis artificiais


		tableau = []
		for i in xrange(0, rows):
			tableau.append(map(float, file.readline().replace('\n','').split(' ')))


		tableau[0] = [-x for x in tableau[0]]


		tmp = ['Z'] + range(n + 2, cols+1)

		for i in xrange(0, rows):
			tableau[i] = [tmp[i]] + [tableau[i][-1]] + tableau[i][0:-1]

		tableau.insert(0, range(2,cols+1))


	# except e:
	# 	print "The file is not in the correct format."
	# 	e.print()

	return n, m, tableau



