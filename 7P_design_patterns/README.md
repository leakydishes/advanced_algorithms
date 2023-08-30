## Bounded and Unbounded Knapsack

### Aim of module
I explored unbounded and bounded (0/1 knapsack) problem, I big part of this week’s learning was solidifying how to check we are using Dynamic Programming and breaking down problems into sub-problems. Additionally, I learnt how to create a function for my tests to reduce code duplication. I am excited to work on more problems using LCS (Longest Common Subsequence) as I found this was tricky to implement. I am excited to explore both my recursive and DP climbing stairs solution with my lecturer. 

#### Dynamic Programming:
- Involves identifying optimal sub-structures and leveraging overlapping subproblems.
- Implements a systematic way to extract substructures and build solutions.
- Provides a bottom-up approach to building the final solution, storing subproblem solutions in a table.

#### Climbing Stairs:
- A problem where you can take 1, 2, or 3 steps at a time to reach the top.
- Recursive solution based on Fibonacci sequence: step(n) = step(n-1) + step(n-2).
- Dynamic programming bottom-up approach reduces complexity to O(1).

## Test Case Time Complexity
#### Possible ways to climb 20 steps
- Recursive (Brute Force): 10946
- Dynamic Programming (DP - Array): 10946

#### Comparison
- Brute Force Time: 0.006150 Seconds
- Dynamic Programming (DP - Array): 0.000111 Seconds
- The DP algorithm is much faster (by 0.006039 seconds) than the brute force recursion algorithm.
- The time difference between the two is more significant the higher number of n (steps).
- Even though DP is faster as it uses an Array it would be using more memory then the recursive approach.


#### Longest Common Subsequence DP Formulation:
- Focuses on finding the length of the longest common subsequence (LCS).
- Uses a 2-dimensional table to break down the problem by decrementing the lengths of input sequences.
- Solves for the length of the LCS in O(nm) time.
- Can recover the LCS using the table after finding its length.

##### LCS Algorithm - Matrix-based Approach (2D)
- Creates a path of the length of longest common subsequence.
- Then backtracks from bottom-right to the top left corner, to find all LCS.
- If subset 1 (value) is in subset 2 (value) they are part of LCS.
- If value is different we go up or left, depending on which cell has a higher number.
- Creating a matrix c[i][j] represeting lengths of LCS X[i] and Y[j]

#### Unbounded Knapsack Problem:
- Solvable in O(nW) time, where n is the number of items and W is the capacity of the knapsack.
- Utilizes dynamic programming to create a solution.
- Uses a 1-dimensional table to break down the problem into smaller subproblems by reducing the knapsack size.

##### Unbounded
 ![unbounded_knapsack](https://github.com/leakydishes/advanced_algorithms/assets/79079577/a4158f97-da9d-4951-9eac-9e54b4e8e3ae)

#### Bounded Knapsack (0/1 Knapsack):
- Differs from unbounded knapsack by allowing only one copy of each item to be used.
- Uses a dynamic programming approach as well.
- Cannot use the same subproblem as unbounded knapsack with a smaller knapsack.
- Requires tracking which items have been used and which haven't.

##### Bounded (0/1 Knapsack)
![bounded_knapsack](https://github.com/leakydishes/advanced_algorithms/assets/79079577/e2deb935-77a3-4492-8fbb-0cb3657a3962)

#### Knapsack Problem:
- Involves packing items with weights and values into a knapsack with a given capacity.
- Two variants: unbounded (allows multiple copies) and 0/1 (one copy of each item).
- Utilizes dynamic programming to solve, identifying optimal substructures and overlapping subproblems.

#### 0/1 Knapsack Problem Bottom-Up DP:
- Solves the knapsack problem with a 0/1 constraint using a dynamic programming approach.
- Uses a 2-dimensional array to store optimal values for different numbers of items and capacities.
- Solves the problem iteratively, building on solutions to smaller subproblems.
- Achieves time complexity of O(nw), where n is the number of items and w is the capacity.


##### References:
    * Data Structures & Algorithms in Python - GoodRich, 2013: Dynamic Programming 13.3
    * https://www.youtube.com/watch?v=jlCJqgSgXI4 
    * https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    * https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/ 
    * https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    
