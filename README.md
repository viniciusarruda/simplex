# Simplex

## Directory structure

```
|- in: Input files with the linear programming problems.
|- out: Where the output of the inputs of `in` directory will be placed.
	|- .keep: Help file to force git to push an empty folder.
|- src: Source code.
	|- main.py: Tableau set up.
	|- simplex.py: Handles the tableau.
	|- tableau.py: Provides the basic operations to perform on tableau.
|- description.pdf: Assignment description (in brazilian portuguese).
|- README.md: This readme file.
|- run.sh: Bash script to solve the problems placed in directory `in`.
```

## About

This was an assignment of Linear Programming and Introduction to Optimization, and the aim was to write the simplex and two-phase simplex algorithms to solve linear programming problems.  

The given linear problem must be in "standard form" as below:

```
minimize:
	z = cx
subject to:
	Ax = b
where:
	b ≥ 0, x ≥ 0, x ∈ R, c ∈ R, b ∈ R and A_{m×n}
```

The input file must be structured line by line as below:

1. A key indicating the choice between simplex or two-phase simplex, being 1 for simplex and 2 for two-phase simplex.
1. The number of lines followed by the number of columns that the matrix data above has.
1. If key is 2, then the matrix must contain the line related to the artificial objective function and the columns related to the artificial variables.

## Example of input

#### Simplex

The linear programming problem below:

```
minimize:
	z = 2x1 - 4x2 + 3x3
subject to:
	 x1 + x2 +  x3 ≤ 4
	      x2 - 3x3 ≤ 3
	6x1 - x2 +  x3 ≤ 4
	    x1, x2, x3 ≥ 0
```

Then, putting at the "standard form":

```
minimize:
	z = 2x1 - 4x2 + 3x3
subject to:
	     x1 + x2 +  x3 + x4           = 4
	          x2 - 3x3      + x5      = 3
	    6x1 - x2 +  x3           + x6 = 4
	           x1, x2, x3, x4, x5, x6 ≥ 0
```

Will give the respective input:

```
1
4  7
2 -4  3  0  0  0  0
1  1  1  1  0  0  4
0  1 -3  0  1  0  3
6 -1  1  0  0  1  4
```

#### Two-Phase Simplex

The linear programming problem below:

```
minimize:
	z = 2x1 - 4x2 + 3x3
subject to:
	 x1 + x2 +  x3 ≤ 4
	      x2 - 3x3 ≤ 3
	6x1 - x2 +  x3 ≥ 4
	    x1, x2, x3 ≥ 0
```

Then, putting at the "standard form":

```
minimize:
	z = 2x1 - 4x2 + 3x3
subject to:
	 x1 + x2 +  x3 + x4           = 4
	      x2 - 3x3      + x5      = 3
	6x1 - x2 +  x3           - x6 = 4
	       x1, x2, x3, x4, x5, x6 ≥ 0
```

Then, we have the function z^a = x1^a:

```
minimize: 
	z^a = x1^a
	  z = 2x1 - 4x2 + 3x3
subject to:
	 x1 + x2 +  x3 + x4                  = 4
	      x2 - 3x3      + x5             = 3
	6x1 - x2 +  x3           - x6 + x1^a = 4
	        x1, x2, x3, x4, x5, x6, x1^a ≥ 0
```

Will give the respective input:

```
2
5  8
0  0  0  0  0  0  1  0
2 -4  3  0  0  0  0  0
1  1  1  1  0  0  0  4
0  1 -3  0  1  0  0  3
6 -1  1  0  0 -1  1  4
```

## How to run 

1. Open the terminal.
1. Got to the simplex directory.
1. Run the command:
```
python src/main.py <path of file with standard form>
```

## Automatic run

Run the script `run.sh` as `bash run.sh` to run all the files in `in` directory, putting the output in `out` directory with the same name.

## Adding a new file

If is desired to include a new file, just format it in "standard form" and name it as `file#` where `#` is the next non-existing number.
