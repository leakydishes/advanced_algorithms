### Activity Selection Problem - Greedy
- The greedy strategy sorts the activities based on their end times and selects the activity with the earliest end time first.
- It iteratively selects activities that do not overlap with the previously selected ones.
- This approach aims to make a locally optimal choice at each step by selecting the activity that ends earliest, without considering the global picture.

#### Select a maximum number of non-overlapping activities to perform. 
- Algorithm has inputs:
- activities (list of activities)
- start_times (list of start time for the activities)
- end_times (list of end times for the activities)

- The Activity Selection Problem Algorithm uses an empty list to store activities.
- The function zip in python is used to create tuples (end_time, start_time, activitiy) and then sorting based on end times.

#### Implementation
1. The first activity in the sorted list is going to be non-overlapping with the others, so its added to selected_activities list.
- the end_time for this activity is stored in prev_end_time variable.
2. The loop iterates through the remaining activities in the sorted list
- For each acitvity it checks if start time of the current activity is > = to the prev_end_time (of last selected activity). 
- If true, current activity is considered non-overlapping and added to selected_activities list and pre_end_time updated. 
3. The selected_activities list contains all the activities that were selected, the length of this list represents the max number of non-overlapping activities that can be performed in a day!


### Activity Selection Problem - DP
- Dynamic Programming Solution - Activity Selection
- This algorithm takes same inputs
- Uses same n variable to store total number of activates. 
- Instead of using a list, use an array max_activities of length n, with all values set to 1. 
- Each element of the array will eventually store max number of activities that can be selected.

#### DP part 
- uses nested loops to fill in the max_activities (array).
- Outerloop iterates over each activity starting at second. 
- Inner loop iterates over the activities that follow the current one.
- The overlapping activities are checked if the end time of activity j is < = to the start time of activity i. 
- Ensuring activities don't overlap.
- max_activities[i] and [j + 1] is updated to be the max current value.
- when array is full use max(max_activities)
- Finds the max number over non-overlapping activities.
- Reconstructs the list based on max_activities array using correct corresponding activity to selected_activity list.
##### Backtracks to find the remaining selected activities by decrementing max_selected, final score is reversed to get correct order and count.

#### Difference in results
- When you create overlapping activities, the greedy strategy may not always find the optimal solution.
- Greedy can produce suboptimal results, as it makes locally optimal choices at each step without considering the global picture unlike Dynamic programming solution.


### Time Comparison: Activity Selection & DP Solution
##### Non-overlapping activities
- Greedy Time: 0.000092 seconds
- DP Time: 0.000108 seconds
	- Both DP and Greedy algorithm selects the optimal solution A and C
	- Greedy Time is slightly faster than DP time

##### Overlapping activities
- Greedy Time: 0.000063 seconds
- DP Time: 0.000061 seconds
	- Greedy selects A, C, E as solution
  	- DP selects B, D, E as solution
	- Greedy doesn't always find optimal solution
  	- DP finds optimal solution
	- DP is slightly faster, a larger graph would show a bigger difference in time

##### Summary
- Non-overlapping both Greedy and DP create similar results, Greedy is faster
- Overlapping DP more successful then Greedy in finding optimal solution, minimal time difference

### Prim’s Algorithm O(mlog(n))
- Prim's algorithm is a greedy algorithm used to find the Minimum Spanning Tree (MST) of a connected, undirected graph.
- The MST is a subset of the edges of the graph that forms a tree and includes all the vertices while minimizing the total edge weight.
-  Prim's algorithm starts with an initial vertex and grows the MST one vertex at a time by selecting the edge with the smallest weight that connects a vertex in the MST to a vertex outside the MST.

##### The algorithm (Prims) starts by initializing a key (distance) and parent for each vertex in the graph.
- Make each node store a value (key) k[x]
- Key makes decision to include node or not in Minimum spanning tree.
##### The key is initially set to positive infinity to represent that the vertices are not yet in the MST.
- The parent is initially set to None.
- Initialise values (to infinity) for all nodes except root.
	- Store one more value for each vertex P[x] -> pointing to nearest node on minimum spanning tree.

##### Setting the Key for the Starting Vertex:
- The key of the starting vertex s is set to 0 to make it the first vertex in the MST.
##### Empty MST/ Priority Queue:
- An empty list MST is created to store the edges of the MST.
- A priority_queue is initialized with the vertices of the graph.
- The vertices are sorted based on their keys (initially all infinity), so the starting vertex s is at the top of the priority queue.

##### Loop:
- The algorithm enters a loop that continues until the priority queue is empty.
- Each iteration of the loop, it extracts the vertex u with the smallest key from the priority queue.

##### Adding Edges to MST:
- If u has a parent (i.e., it's not the starting vertex), the edge (u.parent, u) is added to the MST.
- The edge connects a vertex inside the MST to a vertex outside the MST.

##### Updating Keys and Parents:
- The algorithm then examines all neighbors v of vertex u and checks if the edge weight from u to v is smaller than the current key of v.
	- If it is, the key of v is updated with the smaller weight, and the parent of v is set to u.
  	- Grows the MST by considering the smallest-weight edges that connect the MST to the remaining vertices.
##### Updating Priority Queue:
- After updating the keys and parents, the priority queue is adjusted to reflect the changes.
- priority_queue ensures that the vertex with the smallest key is always at the front.
- priority_queue empty, the algorithm has constructed the MST, and it returns the list of edges in the MST.
##### Similar to Dijkstra’s algorithm!
- Differences:
1. Keep track of p[v] in order to return a tree at the end
- But Dijkstra’s can do that too, that’s not a big difference.
2. Instead of d[v] which we update by
	- d[v] = min( d[v], d[u] + w(u,v) )
- we keep k[v] which we update by
	- k[v] = min( k[v], w(u,v) )

#### Time Comparison slowPrim and Prim Algorithm
- Both algorithms find MST (A - C, A - B)
- slowPrim is slower in finding MST then prim algorithm.
- Prim algorithm is more efficient then slowPrim in this case, a larger graph would show a greater time distance. 



