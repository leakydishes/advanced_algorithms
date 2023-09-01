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

### Prim’s Algorithm
Time Comparison slowPrim and Prim Algorithm
- Both algorithms find MST (A - C, A - B)
- slowPrim is slower in finding MST then prim algorithm.
- Prim algorithm is more efficient then slowPrim in this case, a larger graph would show a greater time distance. 



