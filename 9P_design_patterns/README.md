## Graphs
Finding the shortest path between two nodes in a graph has two factors:
1.	If you have weights on the edges – normally non-negative w(u, v)
2.	If you have no weights on the edges (determine using number of edges between the two nodes)

#### Dijkstra Shortest Path:
u and v in weighted graph = Cost of path (sum of weights along that path)
-	Node A, Node B (shortest path between nodes is sum of weights on path between A, B).

#### Dijkstra algorithm 
d[v] = min(d[v],d[u] + edge Weight (u,v))
- Single-Source Shortest Path Algorithm
- Selects one node (root) and build a search based on the selected node using greedy approach
- When considering neighbours of u, do not consider neighbours that have already been explored (‘sure’ status)

To find the shortest path between a node to all other nodes:
-	Each node stores a table with length of the shortest path from that node to all other nodes in the graph. 
-	Shortest path (cost) and map to traverse the shortest path. 
1.	Pick a node with smallest value in matrix d, labelled ‘I’m not sure yet’ status (smallest estimate path to current node). 
2.	Update the neighbours of u
3.	Mark current node u as explored ‘sure’, other nodes update based on distance (u with min d[u])
4.	Repeat analysis until all nodes have been explores

#### Dijkstra Issues: 
-	Negative weights – this form of Dijkstra cannot handle this.
-	If weight are changed, Dijkstra must be re-run. 

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/c78dad9f-9d13-41ff-a7a8-1659fdb34dd7)

### Dijkstra Step-by-Step Iteration
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/8744afdc-cd18-4929-b69d-b0516e686d72)

### Bellman-Ford (BF) algorithm 
- A variant of Dijkstra that can handle negative weights – slower. It overestimates the length of the path from the starting node to all other nodes. 
- Finds the shortest paths from a node to all other nodes in a weighted graph, even if it has negative weight edges.
- Negative weight cycle: Sum of edge weights are negative. No labelling of nodes ‘sure/unsure’.
- Select all nodes as neighbours when considering neighbours of u.
- It is the selection of nodes that are to be explored.
- Greedy option – picking only one node during exploration
- Select nodes 1-by-1 a de-centralised algorithm (flexible in changing weights)

#### Algorithm
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/8eb49d48-ac31-401e-b0b8-1fa409687434)

### Bellman-Ford Step-by-Step Iteration
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/c857eeb4-e9fe-4d36-8f7d-e4c08eb1f70c)


#### Bellman Ford Modify Algorithm, detect if there are any negative cycles
-	Run (n + 1 or n + 2) and see if results distance change if they do than exit Bellman Ford.
-	BF can detect negative cycles in graph by observing changes in the estimated distance during the relaxation process. 
-	Negative cycle: cycle in which the sum of the edge weights along the cycle is negative. 
-	IF BF algorithm detects a negative cycle there is no well-defined shortest path since you can keep going and going and going around the cycle and continually decrease the path length. 

## Graphs Running Time Analysis
-	Must keep track of ‘unsure’ nodes using array with operations
	- Dijkstra algorithm: n(T(findMin) + T(removeMin)) + mT(updateKey)
1.	Select a node with minimum estimate of distance, findMin() operation
2.	Remove node that is explored ‘sure’ marked, removeMin() operation
3.	Update value d repeatedly, updateKey() operation

##### Heap (data structure) in Dijkstra:
Dijkstra algorithm: n(T(O(1)) + T(O(log(n)) + mT(O(1))

##### Arrays in Dijkstra:
Dijkstra algorithm: n(T(O(n)) + T(O(n))) + mT(O(1))

##### RB Tree in Dijkstra:
Dijkstra algorithm: n(T(O(log(n)) + T(O(log(n))) + mT(O(log(n))

##### Bellman-Ford Algorithm O(m x n)
* Analyses each edge m, at least n-1 times.

## Dynamic Programming (DP)
Optimal Substructure: Optimal solutions to sub-problems are sub=solutions to the optimal solution of the original problem. Bottom- Up or Top-Down Approach
Overlapping Subproblems: The subproblems show up again and again
-	An algorithm design paradigm, used for solving optimisation problems.
1.	Bellman-Ford Algorithm is a problem-solving strategy – Dynamic Programming (DP)
-	Solution to smaller sub-problem: shortest path to node i relies on the shortest path to node i – 1

2.	Fibonacci Numbers (represent a sequence of numbers with the property that the sum of two consecutive numbers in the sequence formulates the next number in the sequence. 
-	Solution to smaller sub-problem: F(i) we can compute it from F(i-1)

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/12927a7f-99ef-4c7c-8040-9d507860b28d)


### Designing Algorithm for DP:
-	Keep a table of solutions to the smaller problems
-	Use the solutions in the table to solve bigger problems
-	At the end we use information we have collected along the way to find the solution to whole problem. 

#### Bottom-up Approach:
	Fibonacci: Solve problem computing F(0) and F(1) .. F(2) .. F(n-1) … F(n)
	Bellman-Ford: Solve problem d^{(0)}[v] … d^{(1)}[v] … d^{(n-1)}[v] … d^{(n)}[v]

#### Algorithms
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/4ee3aa1f-0007-427f-8fa1-badcd5053f7b)
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/3566e67b-748b-4855-a020-61cec32dc5f2)

#### Top-Down Approach:
-	Recurse to solve smaller problems (memorisation)
-	Keep track of what small problems are already solved to prevent re-solving.
  
#### Algorithm
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/6a281acf-82fe-4572-85b0-65a2eaf6d2b4)


### Floyd-Warshall 
D^{(k)}[u,\ v] =D(k-1)[u,v]
- All-Pairs Shortest Paths (ASPS)
- The shortest path from u to v for all pairs (u, v)  of vertices in the graph
- Find the shortest path between any pair of nodes in the graph.

##### Issue Bellman-ford: for n times has a time complexity
- For all s in G (graph), Run Bellman-Ford on G starting at S. O(n\bullet\ nm)\ =\ O(n^2m)
Floyd-Warshall Algorithm
An algorithm to find the shortest path in a graph, where Bellman-Ford and Dijkstra Algorithms are single-source, shortest path algorithms, Floyd-Warshall computes shortest distance between every pair of vertices in the input graph. 
-	Provides the distance between vertices in a resulting matrix
-	Dependent on the number of vertices in a graph.

### Floyd-Warshall Algorithm
An algorithm to find the shortest path in a graph, where Bellman-Ford and Dijkstra Algorithms are single-source, shortest path algorithms, Floyd-Warshall computes shortest distance between every pair of vertices in the input graph. 
-	Provides the distance between vertices in a resulting matrix
-	Dependent on the number of vertices in a graph.
  
### Algorithm
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/324389a6-91da-4b73-a11f-d9c6dcb64373)

### Floyd-Warshall Algorithm Complexity
- Running complexity is O(n^3)
- Not better than running Dijkstra n times
- Simpler to implement and handle negative weights
- Storage: store two n-by-n arrays and graph (original)

