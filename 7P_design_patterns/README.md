## Bounded and Unbounded Knapsack

### Aim of module
This week I explored the unbounded and bounded (0/1 knapsack) problem, I big part of this week’s learning was solidifying how to check we are using Dynamic Programming and breaking down problems into sub-problems. Additionally, I learnt how to create a function for my tests to reduce code duplication. I am excited to work on more problems using LCS (Longest Common Subsequence) as I found this was tricky to implement. I am excited to explore both my recursive and DP climbing stairs solution with my lecturer. 

#### Unbounded Knapsack Problem:
- Solvable in O(nW) time, where n is the number of items and W is the capacity of the knapsack.
- Utilizes dynamic programming to create a solution.
- Uses a 1-dimensional table to break down the problem into smaller subproblems by reducing the knapsack size.

#### Bounded Knapsack (0/1 Knapsack):
- Differs from unbounded knapsack by allowing only one copy of each item to be used.
- Uses a dynamic programming approach as well.
- Cannot use the same subproblem as unbounded knapsack with a smaller knapsack.
- Requires tracking which items have been used and which haven't.

#### Dynamic Programming:
- Involves identifying optimal sub-structures and leveraging overlapping subproblems.
- Implements a systematic way to extract substructures and build solutions.
- Provides a bottom-up approach to building the final solution, storing subproblem solutions in a table.

#### Longest Common Subsequence DP Formulation:
- Focuses on finding the length of the longest common subsequence (LCS).
- Uses a 2-dimensional table to break down the problem by decrementing the lengths of input sequences.
- Solves for the length of the LCS in O(nm) time.
- Can recover the LCS using the table after finding its length.

#### Knapsack Problem:
- Involves packing items with weights and values into a knapsack with a given capacity.
- Two variants: unbounded (allows multiple copies) and 0/1 (one copy of each item).
- Utilizes dynamic programming to solve, identifying optimal substructures and overlapping subproblems.

#### Climbing Stairs:
- A problem where you can take 1, 2, or 3 steps at a time to reach the top.
- Recursive solution based on Fibonacci sequence: step(n) = step(n-1) + step(n-2).
- Dynamic programming bottom-up approach reduces complexity to O(1).

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
    
