##  Algorithm Analysis

### Algorithmic Complexity
Data structures are important to make informed
decisions [1], [2]
o An agreed arrangement, so that’s it’s easy to
store as well as find the desired items

- Algorithms are created to store and retrieve data in
the most efficient way
o Data can be stored in cloud, database, data
center etc.

- Sorting algorithms
o Merge sort, insertion sort, quick sort, heap sort, bucket sort etc.
- Algorithm Complexity
o Efficiency of storing and retrieving data from a data source
o Data can be stored in memory, database, SQL or NoSQL etc.
- Which algorithm is best?
o Big O Notation to categories an algorithm
o Always present worst case

- 𝑂(𝑛) Complexity
o 𝑛 => number of items
o At worst case, it will have to search ‘𝑛’ items to find the desired one
o Starting at front of array ‘𝑛’ items and find the last ‘𝑛 -1’ item in array
o 𝑛 items = 𝑛 steps
- 𝑂𝑛! / 𝑂(𝑛 ∙ 𝑛) Complexity
o 𝑛 => number of items
o Worst case, it will have to perform 𝑛 ∙ 𝑛 steps to find the desired one
𝑛 = 1 stack of shirts (3 x shirts), 𝑛 = 1 stack of pants (3 x pants), match each item
3 + 3 + 3 = 9
3 ∗ 3 = 0
3! = 9

- 𝑂(𝑛 ∙ 𝑚) Complexity
o 𝑛 => number of items
o Worst case, it will have to perform 𝑛 ∙ 𝑚 steps to find the desired one
𝑛 = 1 stack of shirts (3 x shirts), 𝑚 = 1 stack of pants (2 x pants), match each item
2 + 2 + 2 = 6
3 ∗ 2 = 6

- 𝑂(𝑙𝑜𝑔 𝑛) Complexity
o 𝑛 => number of items
o Worst case, it will have to perform 𝑙𝑜𝑔 𝑛 steps to find the desired one
Example: As your number of items grow (very slowly), your number of steps grow,
BUT it is not exponential it is logarithmic
No matter how big the dictionary is, you can find a word in 2 or 3 steps, must be
stored in a sorted order. Binary search tree (sorted elements)
𝑙𝑜𝑔 (10) = 1 (steps)
𝑙𝑜𝑔 (100) = 2 (steps)
𝑙𝑜𝑔 (1000) = 3 (steps)

- 𝑂(𝑛 𝑙𝑜𝑔 𝑛) Complexity
o 𝑛 => number of items
o Worst case, it will have to perform 𝑛 ∙ 𝑙𝑜𝑔 (𝑛) steps to find the desired one
𝑛 = 1 stack of shirts (3 x shirts), 𝑙𝑜𝑔 (𝑛) = Items in store, match each item
Go to a store to find the match. Even if the store has hundred items, we can find
items in a few steps as they are in sorted order (number, colour etc)
3 ∗ (2 − 5 matches)
  n*logn

O(…) means a UPPER bound
- Is basically the UPPER BOUND
- 𝑇(𝑛) is the runtime: positive and increasing in n
- 𝑇(𝑛) 𝑖𝑠 𝑂(𝑔(𝑛)) if g(n) grows at least as fast as 𝑇(𝑛) as 𝑛 gets large!

𝛀(…) means a LOWER bound
- 𝑇(𝑛) 𝑖𝑠 Ω(𝑔(𝑛)) if g(n) grows at most as fast as
𝑇(𝑛) as 𝑛 gets large!

𝛉(…) means both (lower/ upper) bound
- 𝑇(𝑛) 𝑖𝑠 θ(𝑔(𝑛)) if,
𝑇(𝑛) = 𝑂C𝑔(𝑛)D
and
𝑇(𝑛) = Ω(g(n))

### Asymptotic Analysis
algorithm, how much time an algorithm
takes with a given input 𝑛 [3]
1. Big 𝑂 – worst case running time
2. Big Theta 𝜃
3. Big Omega Ω – best case running time
- Compute the Big 𝑂 of an algorithm by counting the
number of iterations the algorithm always takes
with an input of 𝑛.
- This loop will always iterate 𝑛 times for a list of 𝑛
for each item in list:
print item
- If algorithm contains many parts – describe runtime
based on the Slowest part of program
- Common runtimes –
- Constant 𝑂(1)
- Logarithmic 𝑂(log 𝑛)
- Linear 𝑂(𝑛)
- Polynomial 𝑂(𝑛!)
- Exponential 𝑂(2")
- Factorial 𝑂(𝑛!)
- Speed of algorithm measured using while loop
o Loop can be used to count the number of iterations it takes a function to
complete
- Queue data structure based on ‘First in First Out Order’ taking 𝑂(1)runtime
Constant
o To retrieve the first item in a queue
- Stack data structure is based on ‘First in Last out order’ taking 𝑂(𝑛)runtime Linear
o To retrieve the first value in a stack, all the way at the bottom!

##### Max Value Search in List
o For locating the maximum value in a list of
size 𝑛 is 𝑂(𝑛) Linear
§ Due to the entire list of 𝑛 items being
traversed

##### Bubble Sort
- Simplest sorting algorithm for a list
- Every item in list, compares it with its subsequent neighbor and swaps them if they
are in descending order
- Each pass of swap takes 𝑂(𝑛), there are 𝑛 items in list, taking 𝑂(𝑛 ∙ 𝑛) swaps
- Big 𝑂 = 𝑂(𝑛!)

##### Insertion Sort
- The outer for loops takes n-1 iterations
- The inner while loop (worst case) runs for n
iterations
o Complexity of insertion sort to be n2
o Merge sort is better

##### Merge Sort
- Divide and conquer approach
- Recursive approach and divides each
problem into two equal sized halves
- Iteration of merge sort divides the problem
into half, the length of divisions = log(n)
o Complexity O(n log n)

##### Divide and conquer creates unbalanced division of work
- Quick sort: selection pivot controls size of two blocks
- Maximum-subarray problem
- Square matrix multiplication problem

##### Division resulting in three + sub problems
- Assuming log has base 2
- If more than two subproblems consider log(k), k is number of sub problems.
- Systematic way of finding these complexities

### Recurrences
- Is an equation or inequality that describes a function in terms of its value on smaller
inputs.
- Solution 𝑇(𝑛) = 𝑂(𝑛 log(𝑛))

Recurrence says when the problem size is of size 1, it is in constant time.
- If 𝑛 > 1, algorithm breaks the input into sub-problems each operation on n/2 size of
the data.
- The sub-problem spends 𝑂(𝑛) time other than just breaking the bigger problem into
sub-problems.
- A recursive algorithm might divide subproblems into unequal sizes, such as 2/3 to
1/3 split. If the divide and combine streps take linear time.
o This would rise the recurrence 𝑇(𝑛) = 𝑇(2𝑛/3) + 𝑇(𝑛/3) + 𝑂(𝑛)
Subproblems are not necessarily constrained to being a constant fraction of the original
problem size.
- A recursive version of linear search would create just one subproblem containing
only one element fewer than the original problem
- Would take constant time plus the time for the recursive calls it makes T(𝑛) =
𝑇(𝑛 − 1) + 𝑂(1)
- Merge sort on 𝑛 elements when 𝑛 is odd, we end up with subproblems of size
floor M"
!N and ceil M"
!N
o Neither size is actually M"
!N, because M"
!N is not an integer when 𝒏 is odd!

#### Boundary conditions
- Running time of an algorithm (constant-sized input is a constant) T(𝑛) = 𝑇𝑂(1) for
small 𝑛. *State or solve recurrences omit floors, ceilings, and boundary conditions

#### Recurrence Relations
- A formula for 𝑇(𝑛) where 𝑇(𝑙𝑒𝑠𝑠 𝑡ℎ𝑎𝑛 𝑛)
- Given a recurrence relation for 𝑇(𝑛), find a closed form expression for 𝑇(𝑛)
- Think of 𝑇(1) in terms of complexity, 𝑇(1) = 𝑂(1), constant etc
o Base Case, not as important when it is constant.
o Result: 𝑇(𝑛) = 𝑂(𝑛𝑙𝑜𝑔(𝑛))

#### Merge sort
Formulate a recurrence relation of the merge sort:
1. If we have solved the two subproblems of size M"
!N, it takes us 11𝑛 operations to find
result.
o The use of 11 is arbitrary, it could 10 or 5, order is O(n).
- 𝑇(𝑛) where 𝑇(𝑙𝑒𝑠𝑠 𝑡ℎ𝑎𝑛 𝑛)
2. Find a closed form expression for T(𝑛), that is 𝑇(𝑛) = 𝑂(𝑛 log(𝑛))

### The Substitution Method
A method guaranteed to find right result.
1. General Substitution Approach
2. Substitution based on Induction
General substitution approach
- Recurrence Merge Sort:
𝑇(𝑛) = 2 𝑇 M
𝑛
2
N + 𝒏
or
𝑇(𝑛) = 2 𝑇 M
𝑛
2
N + 𝑶(𝒏)
- See PDF for example and explanation
  
##### Substitution based on induction
1. Maintain a loop invariant – true at every iteration
2. Proceed by induction
Four steps in the proof by induction:
1. Inductive Hypothesis: The loop invariant holds after the 𝑖$% iteration
2. Base case: The loop invariant holds before the 1st iteration
3. Inductive step: If the loop invariant holds after the 𝑖$% iteration, then it holds after
the (𝑖 + 1)&$ iteration
4. Conclusion: if the loop invariant holds after the last iteration, then we win!
- Solve merge sort recurrence formulation via substitution methods.
- Formulate recurrence,

##### Linear Recurrence
- 𝑛 decreases from 𝑛 to 𝑛 − 1
- Solve recurrence using substitution method
- Expand term 𝑇(𝑛)
- See PDF for example and explanation

##### Unbalanced Recurrences
- Can use computing complexity via induction BUT
- Akra-Bazzi is GUARANTEED to work in a multitude of problems
- Solving via substitution becomes complex
- Use Akra-Bazzi method
- See PDF for example and explanation

##### Substitution based on Induction
Substitution method for solving recurrence comprises two steps,
1. Guess the form of the solution. Requires substantial experience (guess the form of
the answer to apply it, use some heuristics) or you can use recursion trees to
generate good guesses
2. Use mathematical induction to find the constants and show that the solution works.
* 𝑐 = constant
- Guess: Solution = 𝑂(𝑛 log(𝑛))
o 𝑇(𝑛) = 𝑂(𝑛 log(𝑛))
- Prove 𝑇(𝑛) <= 𝑐 𝑛 log 𝑛, where 𝑐 > 0
* Holds true to for all positive 𝑚 < 𝑛 , where 𝑚 = "
!
- Thus, 𝑇 M"
!N < = 𝐶 ("
!) log("
!)
- See PDF for example and explanation
  
### The Master Theorem
- Sub class problems use The Master Theorem method.
- Solves recurrence when all of the subproblem are of equal sizes.
- 1. a: number of subproblems
- 2. b: factor by which input size shrinks
- 3. d: need to do 𝑛, work to create all subproblems and combine solutions
- See PDF for example and explanation
  
### The Recursion Tree Method
Most popular application, use before The Substitution Method or The Master
Theorem!
- Each node represents the cost of a single subproblem (within the set of recursive
function invocations)
- Sum the costs within each level of tree to obtain a set of per-level costs
- Sum all the per-level costs to determine the total costs of all levels of the recursion
“A recursion tree is best used to generate a good guess, which you can then verify by the
substitution method. When using a recursion tree to generate a good guess, you can often
tolerate a small amount of “sloppiness,” since you will be verifying your guess later on. If
you are very careful when drawing out a recursion tree and summing the costs, however,
you can use a recursion tree as a direct proof of a solution to a recurrence.” [4]
- See PDF for example and explanation
  
### The Select(A, k) problem
The Select(A, k) Problem
- Selects the 𝑘 smallest element in a list 𝐴
- A is a list of distinct elements
- If 𝑘 = 0, returns smallest element in list
- If 𝑘 = 𝑛 = 𝑙𝑒𝑛(𝐴), returns the maximum
element
- 𝑆𝑒𝑙𝑒𝑐𝑡(𝐴, 𝑛/2), returns the median element
If you cannot sort (list is large and distributed across multiple machines), write the function
by keeping track of minimum element, then traverse through list.
- Complexity 𝑂(𝑛)

- Find minimum element
- Keep track of two elements, minimum and second
minimum
- Find median element
- Keep track of "
! set of minimum element in list
- Complexity 𝑂(𝑛!)
o Merge sort has complexity 𝑂
Rely on Divide and Conquer (recursive formulation) resulting in recurrences.
- See PDF for example and explanation
  
Apply Median of Median Method for Pivot Selection
- Median breaks list into two subproblems
- Complexity 𝑂(𝑛), linear
- Break list, each sub-list has 5 elements
- Compute medium of each list, compute
median of the medians
- Median of the median used as the pivot
- See PDF for example and explanation


