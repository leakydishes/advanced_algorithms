##  Network Based Algorithms

This module allowed me to explore graph theory and to understand network related problems in advanced algorithms. A cut is defined as a set of edges removal that divides a connected graph into two non-overlapping (disjoint) subsets [1]. The minimum cut (min-cut) is defined as the minimum number of edges, this divides a graph into two disjointed sets. A randomised contract algorithm known as Karger’s Algorithm is used to find the minimum cut of a graph. But the runtime of this algorithm is deterministic, on every run the time to execute will be limited by a fixed time function (the input), with a small probability of wrong answers being produced. I spent extra time researching mark down for Google Collab to write out the pseudocode [1]. 

In the first activity I explored Karger’s algorithm and modified it to incorporate weighted edges. This modification allowed the algorithm to find the minimum cut that minimises the total weight of edges to be removed. In my research I found the best way of adjusting the edge selection was about iteratively contracting (merging) edges and then testing the returning weighted minimum cut, I changed the original pseudocode given in the module to reflect this. This modification made sure edges with higher weights were more likely to be chosen, using priority queue this time complexity could be O(n*Log(E))

In activity 2 I implemented the Ford-Fulkerson algorithm, which finds the maximum flow in a flow network. I created a directed graph with edges (Capacities, Flow values) with the aim to find the max flow from s (source node) to t (sink node). I started with initial flow of zero which iteratively increases the flow by finidng augmenting paths in the residual graph. The findpath() method uses BFS to search for paths, returning the path and flow value. The ford Fulkerson() method repeatedly calls the find_path() until no more paths can be found and maximum flow is reached. The iteration of ford_fulkerson() method updates the flow values and terminates once max flow value is calculated and no more paths can be found. The min_cut method finds the minimum cut of the flow graph, which separate s from t nodes. This is done by using depth-first search to find the nodes reachable from s in the graph. I found creating multiple test cases enabled me to tidy the code and create better structure in my logic. 

### Research
#### Minimum Cut
Graph cut problems: cut is a partition of the vertices into two non-empty parts
- The minimum number of edges required to remove to disconnect the graph into two components. 

A selection of the edges in graph for two disjoint selections of vertices in groups of part 1 & 2. 
- Must have two set of vertices which are disconnected from each other. 

##### Minimum Cut = a cut that has the fewest edges possible. 
##### Global minimum cut. 
- Global as there are no specific specialized vertices of interest.

##### Local version of gloabl minimum cut problem.
- Minimum s-t cut 

##### Minimum Cut Additional Example 	
Split graph into two disconnected components ${A,B,C,D},{E}$ <br> 
Removing edges $B↔C,B↔E,C↔E$
-	Each cut has sum of weights (edges that are removed).
-	If graph is unweighted, only number of vertices have been removed (3).

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/782b9056-1be4-4716-b39b-e11d396f5867)

#### Karger’s Algorithm 
-	Finds global minimum cuts in undirected graphs. 
-	Important in image segmentation
-	Randomized algorithm, (like QuickSort – always correct but slow) 
-	Karger's algorithm on the other hand is always fast but can be incorrect. High probability it won’t be wrong. It’s Simple (and intuitive).

Use a randomized algorithm in cases where the stakes are low and the cost of a deterministic algorithm is high. 
-	Must quantify the uncertainty 

#### Karger's Algorithm 3 Steps: 
1.	Pick a random edge,
2.	Contract the vertices around it,
3.	Repeat process until you have only two vertices left. 
-	Contracting an edge: Make a super-node (super-nodes like Floyd-Warshall Algorithm). All edges, two and from these two nodes are re-directed to these super-nodes.

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/ae907eb0-e7ee-49ce-bff7-84d5ff84406a)

#### Pseudo code Karger’s Algorithm
	Keeps tracks of all nodes and edges, makes super-nodes, and adjust edges.
	Main loop runs n-2 times (n number of vertices).
	The merge() function will take n time
	Time Complexity O(n^2)
Issue of producing a wrong answer 
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/49c56d39-78b7-422a-8cdd-fba4dd3559a5)


#### Karger’s Algorithm Analysis
Is a randomised algorithm to find a minimum cut of a connected, undirected, and unweighted graph. G=(V,E)
	Based on concept of edge contraction, merging tow nodes (u,v), of the graph G into one node which is also termed as a supernode. All the edges connecting either to u and v are now attached to the merged node (supernode) which may result in a multigraph!

#### Karger’s Algorithm 
	Make a copy of G, term this as the contracted graph CG
	While CG contains more than two vertices.
	Select any random edge u↔v from the contracted graph. 
	Contract the edge and merge the vertices u and v into one.
	Remove self-loops (if formed)
	Only two vertices will be remining in the graph and the edges connecting those two vertices represent the minimum cut of the graph. 

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/2b718eae-6673-4282-85a7-c316630b46eb)

#### Using probabilistic analysis
- how many times to run Karger’s algorithm, to produce where p=1-δ,  δ= 0.01,p=0.99,
Probability Karger’s algorithm returns a minimum cut, 
$1/((n/2))$
$Karger’s algorithm correctness (3.6%),  p=1/28=0.036$
How many times to run algorithm, $repeat T= p=1-δ$

#### Formular to determine Karger’s algorithm number of times (T),
$p (not getting a min-cut in T trails)=(1-P)^T$ <br>
$δ=(1-p )^T$  <br>
$δ=e^(-pT)$  <br>
$log δ=-pT$  <br>
$logδ=-1/((n/2)) T$  <br>
$T=(n/2)  log⁡(1/δ)$  <br>

##### Therefore, Running time O(n^2 x(n/2)  log⁡(1/δ)=O(n^4 )

#### Min-cut Max-Flow Theorem
-	Two special vertices (nodes), find a cut such that these two nodes are disconnected. 
-	Weights associated with each edge; minimum cut defined in terms of the sum of weights of the edges that constitute a cut.

###### Min s-t cut 
Find the minim weight, cut s and t
-	Remove paths/ edges from node s to node t
minimum s-t cut separating s rom t with minimum weights.
-	Cut has cost $(4 + 3 + 4 = 11)$

###### max - flow
-	In addition to weight/ compacity each edge has a flow 
1.	The flow on an edge must be less than its capacity. 
2.	At each vertex the incoming flows must equal the out-going flows

- A maximum flow = flow of maximum value from node s to node t
- 11 units has flow from node s to node t
- Value of max flow from node s to node t is equal to the cost of minimum s-t cut

$max⁡〖flow≤min⁡cut 〗$ <br>
$max⁡〖flow≥ min⁡cut 〗$ <br>
Thus, <br>
$max⁡〖flow= min⁡cut $ <br>

$*max⁡〖flow≥ min⁡cut $ (proof by algorithm) <br>

### Ford-Fulkerson Algorithm Part 1
- Finds min cuts and max flows
- Proof by algorithm
#max⁡〖flow≥ min⁡cut $

1.	Start with zero flow
2.	We will maintain a residual graph Gf,
3.	A path from s to t in Gf will give us a way to improve/increase our flow n original graph,
4.	We will continue improving the flow in original graph until there are no s-t paths left in Gf.
- Graph is associated with itself, a set of weights as well as capacities/weights associated with each edge.
		
lemma,
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/6a264181-5019-44ca-adec-1e8a6f09cfb7)

### Ford-Fulkerson Algorithm Part 2
- Find an augmenting path
- Increase flow along that path
- x is the min weight of any edge in path p 
- Repeat until you can’t find any more paths!

- Start with zero flow
- Final paths from node s to t (BFS)
- Repeat process of finding paths between s and t in residual graph until there is none.
- * Each iteration you can modify the flow 
- Output = flow f = optimal/ maximal flow values from s to t
- *To determine the edges constituting the minimum cut, Traverse from node s to other nodes in Gf

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/414eb51b-edcb-4646-9e45-0962ac253173)

![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/c0d8a537-685a-42e2-a1ef-a58ca90237bb)


![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/5a05b2fe-993b-4d8b-a07d-d98df5bcc6da)

-	Max s-t flow is equal to min s-t cut!
-	The Ford-Fulkerson algorithm can find the min-cut/max-flow. 
-	Repeatedly improve your flow along an augmenting path.
-	How long does this take???

### Theorem
-	If you use BFS, the Ford-Fulkerson algorithm runs in time O(nm2)
- The number of times you remove an edge from the residual graph is O(n). 
- There are at most m edges. 
- Each time we remove an edge we run BFS, which takes time O(n+m). O(m), since we don’t need to explore the whole graph, just the stuff reachable from s.
-	If all the capacities are integers, then the flows in any max flow are also all integers. 
-	When we update flows in Ford-Fulkerson, we’re only ever adding or subtracting integers. 
-	Since we started with 0 (an integer), everything stays integral!
