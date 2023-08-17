## Algorithm

### Using following References

### Bidirectional search is used to find the shortest path between source and a destination. 
It operates by essentially running two simultaneous breadth-first searches one from each node. 
When their searches collide, we have a match. Modify code (section 2), do implement finish time using one of the two different implementations of BFS. 
Bidirectional search to speed up the process. Expecting an algorithm that will speed up the search process by half.

#### 1)Bidirectional search
- used to find the shortest path between a source and a destination.
- It operates by essentially running two simultaneous breadth-first searches one from each node.
- When their searches collide, we have a match.
- Design an algorithm for bi-directional search, and then code it in this week's ipynb.

- Bidirectional search aims to speed up the process by performing two searches, one at the start node and the other from the end node. It stops as soon as the two searches meet.
- Reduces the search space and improves path finding.
- In this implementation I used the second BFS provided as it was more detailed.
    - It uses the *Graph* class and its *vertices*, *getOutNeighbours()* that traverse the graph with BFS.

1.	Set the status of all nodes to unvisited, and the start node and end node as visited. They are set to start queue and end queue to perform BFS from both directions.
2.	Bidirectional BFS enters a loop to before this until both queues are empty/ or a meeting point (node) that has been visited from both ends it found.
a.	Forward BFS: In forward direction nodes are visited form the start queue, if neighbor is found it is marked visited from the other end (meeting point found). 
b.	Reverse BFS: In reverse direction nodes are visited from the end_queue. If neighbor is found it is marked as visited from the other end, the loop is broken and meeting_point is set.
c.	Path Reconstraction: If a meeting_point is found the code reconstructs the shortest path by backtracking from that variable (meeting_point) to both start_node and end_node. By following nodes that have been marked as visited in the revise BFS.

#### Test case: 1
- Testing time output of both single BFS/ DFS and Bidiectional Search times
  ![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/08c50324-e9fc-4567-9686-7fa8c387c309)

#### Test Case 2: Create a bipartite Graph
- I used lucid chart first to create a bipartite Graph based on lecture notes and then implemented this.
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/8c1b58a8-5bc0-417c-bafc-88a87f139dfe)


### Modify the BFS code and implement your designed algorithm.
- For the bi-partite graph keep track of a list of each level, and color code. 
- Color nodes: Different colors based on distance.
- If you have a connection between the same color (set of nodes) it is not Bi-Partite. Color code, write a function where you look at the colours in each layer.
- Edge’s function, you have connections in your color. But they all have a color property.
- Check if they have the same color or a different colour to see if the bi-partite is true or not. 

#### (2) Design an algorithm using BFS to determine if a graph is bi-partite.
- Modify the BFS code in this week's lab book and implement your designed algorithm.
- A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.
   - Ref: https://medium.com/nerd-for-tech/is-graph-bipartite-day-76-python-c0c3cdc9585e 
- A dipartite graph the nodes can be sorted into two sets, such that no two nodes within the same set are connected by an edge.
- This algorithm checks if it can mark one of two colours to each node, so that no nodes share the same color.
- Using a colouring coding system to identify if the graph is bipartite.
- For each uncoloured node in the graph
1. Assigns the first colour to the current node (red)
2. Traverses the neighbors of the current node
3. If a neighbor has not been coloured, assign it the opposite colour
4. If a neighbor has already been coloured with same colour as the current node, then the graph cannot be bipartite -> returns false
- Continues assigning colours to uncoloured nodes (checking each for neighbor node colour) until all nodes are colored or a mix is found.
- If at any point a nighbor is found to have the same color as the current node, it shows that the graph cannot be bipartite.
- If a graph is bipartite it shows the nodes being divided into two colour classes, that no two adjacent nodes share the same color.


### Write an algorithm for finding Strongly Connected Components in a graph
- Code about Node and Graph is given to you – you are expected to extend this code. Refer to cloud Deakin page to find the definition of strongly connected components. 
- You will need each vertex to keep track of time we first enter it, time we finish with it and mark is all done. I changed the DFS to increment time due to test case issues.
- In the new DFS algorithm that’s used with the SCC algorithm, it keeps track of the discovery time (when a vertex is first visited) and the finish time (when the vertex and its neighbors have been explored). 

#### Test Case: 1
- If a graph has no edges (disconnected graph) it cannot have strongly connected components, it is only made up of vertices (nodes). 
#### Test Case: 2
- Additionally, if there is only one node it can be considered an SCC.
#### Test Case: 3
- If there is only a single-node SCC which is a node that self-loops it would form one single-node strongly connected component, which can be considered an SCC. 



