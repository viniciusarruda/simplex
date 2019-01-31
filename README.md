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

$$
\begin{align*}
\text{minimize} \enspace z &= cx \\
\text{subject to:} \ \ \ \ \\
Ax &= b,\\
\text{where:} \ \ \ \ \\
b &≥ 0,\ x ≥ 0,\ x ∈ \mathbb{R},\ c ∈ \mathbb{R},\ b ∈ \mathbb{R}\ \text{and}\ A_{m\times n}
\end{align*}
$$

The input file must be structured line by line as below:

1. A key indicating the choice between simplex or two-phase simplex, being 1 for simplex and 2 for two-phase simplex.
1. The number of lines followed by the number of columns that the matrix data above has.
1. If key is 2, then the matrix must contain the line related to the artificial objective function and the columns related to the artificial variables.

## Example of input

#### Simplex

The linear programming problem below:

$$
\text{minimize} \enspace z = 2x1 - 4x2 + 3x3 \\
\begin{align*}
\text{subject to:} \qquad \qquad \qquad \quad&\\
x1 + x2 + x3 &\leq 4\\
x2 - 3x3 &\leq 3\\
6x1 - x2 + x3 &\leq 4\\
x1, x2, x3 &≥ 0
\end{align*}
$$

Then, putting at the "standard form":

$$
\text{minimize} \enspace z = 2x1 - 4x2 + 3x3 \\
\begin{align*}
\text{subject to:} \qquad \qquad \qquad \quad&\\
x1 + x2 + x3 + x4 &= 4\\
x2 - 3x3 + x5 &= 3\\
6x1 - x2 + x3 + x6 &= 4\\
x1, x2, x3, x4, x5, x6 &≥ 0
\end{align*}
$$

Will give the respective input:

$$
\begin{align*}
&1\\
&4\quad\enspace 7\\
&2\ -4\quad\enspace 3\quad\enspace 0\quad\enspace 0\quad\enspace 0\quad\enspace 0\\
&1\quad\enspace 1\quad\enspace 1\quad\enspace 1\quad\enspace 0\quad\enspace 0\quad\enspace 4\\
&0\quad\enspace 1\ -3\quad\enspace 0\quad\enspace 1\quad\enspace 0\quad\enspace 3\\
&6\ -1\quad\enspace 1\quad\enspace 0\quad\enspace 0\quad\enspace 1\quad\enspace 4
\end{align*}
$$

#### Two-Phase Simplex

The linear programming problem below:

$$
\text{minimize} \enspace z = 2x1 - 4x2 + 3x3 \\
\begin{align*}
\text{subject to:} \qquad \qquad \qquad \quad&\\
x1 + x2 + x3 &≤ 4\\
x2 - 3x3 &≤ 3\\
6x1 - x2 + x3 &≥ 4\\
x1, x2, x3 &≥ 0
\end{align*}
$$

Then, putting at the "standard form":

$$
\text{minimize} \enspace z = 2x1 - 4x2 + 3x3 \\
\begin{align*}
\text{subject to:} \qquad \qquad \qquad \quad&\\
x1 + x2 + x3 + x4 &= 4\\
x2 - 3x3 + x5 &= 3\\
6x1 - x2 + x3 - x6 &= 4\\
x1, x2, x3, x4, x5, x6 &≥ 0
\end{align*}
$$

Then, we have the function $$z^a = x1^a$$:

$$
\text{minimize} \enspace z^a = x1^a \qquad \qquad \quad \\
\text{minimize} \enspace z = 2x1 - 4x2 + 3x3 \\
\begin{align*}
\text{subject to:} \qquad \qquad \qquad \quad&\\
x1 + x2 + x3 + x4 &= 4\\
x2 - 3x3 + x5 &= 3\\
6x1 - x2 + x3 - x6 + x1^a &= 4\\
x1, x2, x3, x4, x5, x6,  x1^a &≥ 0
\end{align*}
$$

Will give the respective input:

$$
\begin{align*}
&2\\
&5\enspace\quad 8\\
&0\enspace\quad 0\enspace\quad 0\enspace\quad 0\enspace\quad 0\enspace\quad 0\enspace\quad 1\enspace\quad 0\\
&2\ -4\enspace\quad 3\enspace\quad 0\enspace\quad 0\enspace\quad 0\enspace\quad 0\enspace\quad 0\\
&1\enspace\quad 1\enspace\quad 1\enspace\quad 1\enspace\quad 0\enspace\quad 0\enspace\quad 0\enspace\quad 4\\
&0\enspace\quad 1\ -3\enspace\quad 0\enspace\quad 1\enspace\quad 0\enspace\quad 0\enspace\quad 3\\
&6\ -1\enspace\quad 1\enspace\quad 0\enspace\quad 0\ -1\enspace\quad 1\enspace\quad 4\\
\end{align*}
$$


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
