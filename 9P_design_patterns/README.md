##  Linear Programming
### To solve the LP (Linear Programming) problem using level curves

- The aim of this LP problem is to Maximise while adhering to the constrains.
  - To find the combination of X1 and X2 which it at max within the feasible region (coloured grey). 

1. Plot the level curves for the objective function
2. Identity the feasible region based on the given constraints
3. Find the optimal solution within the feasible region

- I define the ranges for X1 and X2 to create an evenly spaced sample within range 500
- I than creates equations for the constraint lines (X1, X2, X3)
- I plot these constraints on the graph with X1(x-axis) and X2(y-axis)

#### The objective function 4X1 + 5X2 is than plotted with level curves (dashed lines).
- Each level curve represented by dash line corresponds to a value of the objective function.
- The feasible region is the shaded areas where all constrains are satisfied, any point of this region represents a combination of  and 
- The level curves (dashed lines) are the objective function values at different levels, the higher the level the greater the objective function values.
- The optimal solution is the point where the feasible region and highest-level curve touches/ intersects. 
- The feasible region is bounded by constraints 

$$
\begin{eqnarray}
\textrm{max } && 4X_1 +  5X_2 \\
\textrm{subject to } && 2X_1  + 3X_2 \leq 120 \\
&& 4 X_1 + 3 X_2 \leq 140 \\
&& X_1 + X_2 \geq 80 \\
&& X_1 \geq 0 \\
&& X_2 \geq 0
\end{eqnarray}
$$


### Plot the various values of objective function
##### Different values of N on the objective function in the linear problem to see if change N impacted the optimal objective function value.
- 4 values (12,000, 35,000, 50,000 and 70,000) each representing a constraint. 
- The dashed line for teach represents a different objective function value and no optimal solutions in the feasible region. 

### Result
- But as there is no feasible region there are no feasible solutions to optimise.

### Gaussian elimination
- In LU decomposition we want to decompose original into upper and lower triangular matrices,
##### A = LU,
- A is original matrix we want to decompose
- L is lower triangular matrix (we assume it has 1-s in diagonal)
- U is upper triangular matrix

### Gaussian elimination allows three types of operations
1. Swapping two rows
2. Adding multiple of one row to other
3. Multiplying a row with a nonzero number


### Systems of linear Equations
LU Decomposition of a matrix

A set of values for x1, x2, ... xn, that satisfy all of the above equations simultaneously is said to be a solution to these equations. Case where we have n equations and n unknowns.

#### Equations in matrix-vector Ax = b
- A is non-singular, possess an inverse
#####*Can be computationally intensive/ numerical stability.
- Use LUP-Decomposition instead!

#### LU Decomposition
- Inverse of a matrix can only be computed for a full-Rank matrix.
- x is the vector, finding whose value is the goal!
- Find two n x n matrices, L and U such,
- L is lower triangular matrix
- U is upper triangular matrix

### Steps
- Aim is to decompose the original matrix (A) into two triangular matrices, simplifying the process of solving a linear system.
- I used forward and backward substitution in that order as this is the most common approach.

##### Rewrite linear system,
- Define y=Ux
##### Solve following lower-triangular system first
-*Unknown y, process of Forward substitution
##### Solve upper-triangular system
- *Unknown x, process of Backward substitution

### lu_decomposition(A)
A = LU where L is lower and U is upper.
- Takes a square matrix A as input
- Initialises matrices (L) lower triangular and (U) upper triangular of the same size as A
- The function than performs LU decomposition of the matrix A, factors the A into a lower triangular matrix (L) and upper triangular matrix (U)
- Returns L and U

### back_substitution(U, y)
Ly = b
- Takes the lower (L) and a vector b (input)
- Performs forward substitution to solve the equation (Ly = b) for y where L is the lower triangular matrix.
- Iterates through each row of L and calculates the corresponding element of y using the values of L and already calculated elements of y.
- Returns the results of y

### forward_substitution(L, b)
Ux = y
- Takes the upper triangular matrix U and vector y as input
- Performs back substitution to solve the equation (Ux = y) for x where U is an upper triangular matrix. 
- Iterates U (each row) in reverse order and calculates the corresponding element of x, it does this by using values of U and already calculated elements of x
- Returns the results of x

### lu_solve(A, b)
Results in y = Ax
- Takes the matrix A and vector b input
- Performs forward substitution with L to calculate y
- Performs backward substitution with U to calculate the final solution x
- Returns the result of x

## Solve linear program using Simplex 
Matrix form: initial simplex tableau
Find which variable in the first iteration will become a basic variable (most negative)
The largest coefficients in original objective function!
*This column becomes pivot column

$$
\begin{eqnarray}
\textrm{max } && 18X_1 +  12.5X_2 \\
\textrm{subject to } && X_1  + X_2 \leq 20 \\
&& X_1 \leq 12 \\
&& X_2 \leq 16 \\
&& X_1, X_2 \geq 0
\end{eqnarray}
$$
![simplex_1](https://github.com/leakydishes/advanced_algorithms/assets/79079577/6ba26e45-8657-427f-905e-50c102dac3ab)

![simplex_2](https://github.com/leakydishes/advanced_algorithms/assets/79079577/ddc93416-148e-4c71-a502-62d499b8bf7f)

![simplex_3](https://github.com/leakydishes/advanced_algorithms/assets/79079577/96e3cca1-6f22-4a50-a7f2-7cc6f02de3a7)

![simplex_4](https://github.com/leakydishes/advanced_algorithms/assets/79079577/d045bd39-1281-4a82-b401-0b6421d24d0d)

![simplex_5](https://github.com/leakydishes/advanced_algorithms/assets/79079577/3bf80c31-d6f6-4c8e-b314-e49d0d60266d)

![simplex_6](https://github.com/leakydishes/advanced_algorithms/assets/79079577/370cfe3e-ef8a-408f-a6a8-660ad126f29f)

![simplex_7](https://github.com/leakydishes/advanced_algorithms/assets/79079577/6248bc1e-4591-4d16-9b68-ceea0cfa59b4)
