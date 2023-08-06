## BST Implementations with additional like - AVL functions

### Trees
##### Trees are a widely used data structure, particularly for storing information optimally in various applications.
- Trees are a form of graph data structure, and in this module, Binary Search Trees (BST) will be revisited and discussed.
- Balancing is a common issue with trees, and algorithms like AVL and RB trees address this problem.
- Pseudo-code will be used to address balancing and prepare for future modules.
- Trees offer O(log(n)) complexity for insertion, deletion, and search operations, making them suitable for IDS (Insertion, Deletion, Search) operations.
- Preliminary options to store data are either (Sorted) Arrays or (Sorted) Linked Lists.
- *BST – reduces the searching complexity of Linked Lists from O(n) to O(log(n))

### Binary Search Trees (BST)
- Search property, for any subtree (child) rooted at a node, the stuff on the left is smaller and the stuff on the right is greater.
- Simple to implement but does not follow the balance factor.
- The height of the tree is O(n)
- Searching is not efficient for large numbers of nodes.
- Aims to achieve O(log(n)) complexity for Insertion, Deletion and Search (IDS) operations, cases where it can become O(n) due to unbalance
- Follows a rule that every left descendant of a node has a key less than the node, every right descendent has a key larger than the node.
- Traverses down the tree until the key is found or the element is not present.
- The complexity of search is dependent on the height of the tree.
- The height of the tree can be as long as the number of data points, resulting in slow search operations.
- To manage the height (faster search operations), self-balancing BSTs like AVL and RB-Trees are used, tree rotation operations to reduce tree height while maintaining the BST structure.
- Insertion the Search algorithm to find the right place for the new Key.
- Deletion uses the Search algorithm to find the right place for the new Key

#### Runtime Complexity BST
- Worst-case O(n) – due to unbalance
- Best-case O(1)
- Average is O(log(n))
- Worst-case space complexity O(1)
- *n is the number of nodes in the BST


### AVL
##### Is a self-balancing Binary Search Tree, where the difference between heights of left and right subtrees cannot be more than 1 for all notes. 
- The balance factor if 0, 1 and -1 [2].
- AVL has height (depth of tree) O(log(n)).

- Searching is efficient because searching for the desired nodes is faster due to the balancing of the height. 
-	AVL tree structure consists of 4 fields: subtree, data, right subtree, and balancing factor [2].
-	AVL Insertion/ deletion is complex due to multiple rotations needed to balance tree. 
-	AVL trees are designed to balance a Binary Search Tree after every insertion and deletion operation, resulting in a balanced tree.
-	The height-balance property for AVL tree states that for every node in the tree, the heights of its children differ by at most 1 or at least -1. 
-	Subtrees of an AVL tree are also AVL trees, this property helps in keeping the height of the tree small.
-	AVL trees rely on rotation operations (right, left, left-right, right-left) to maintain the height-balance property, Fig.2-5 drawn in Lucid Chart. 
-	Insertion/ deletion involves finding the right place for the new element and then performing rotations to maintain the AVL property.
-	Insertion/ deletion depending on the situation all four rotations may be used during AVL tree insertion.


##### Single Right Rotation
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/53d7128c-e911-445a-8c16-7ede74e01e42)

##### Single Left Rotation
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/f7508062-bb11-4af9-b725-cc65766e215a)

##### Right-Left Rotation
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/64c9f1ae-4f4a-4deb-8ab3-ce18ca02d432)

##### Left-Right Rotation
![image](https://github.com/leakydishes/advanced_algorithms/assets/79079577/ae3a56be-4e91-4494-a3f0-ae31d9745e35)

### Red-Black Tree (RB-Tree)
-	A self-balancing Binary Search Tree (BST) with an internal mechanism to maintain balance through colour labelling of nodes as red or black. 
-	Have a property that black nodes are balances, red nodes are spread out leading to well-balanced trees.

##### RB-Tree Rules
-	Every node is red or black
-	The root node is black
-	NIL children count as black nodes
-	Children of a red node are black nodes (red property)
-	All paths from a node to NIL nodes have the same number of black nodes (black depth property)

##### RB-Tree Insertion
-	3 steps are involved in this operation
1.	Normal BST insertion
2.	Colouring the new node red
3.	Performing post-insertion operations to maintain RB-Tree Properties

##### RB-Tree Post-Insertion Operations
-	RB-INSERT-FIXUP ensures the tree remains a legitimate RB-Tree by applying rotations and colour adjustments.


##### RB-Tree Deletion
-	Complicated procedure as the tree maintains self-balance after the node is removed while satisfying all the properties of RB-Tree. 
1.	Locate the Node to be Deleted
2.	Adjust the Colours and Fix Property violations
3.	Handle the four cases if property violated
o	Cases involve rotations, colour adjustments to maintain balance while restoring black height property. 
4.	Recurse upward and repeat
5.	Final adjustments

- o	If the root node becomes ‘double black’ you make it single black
- o	Ensure root node is always satisfying RB-Tree Property.


### Bibliography
- [1] 	S. Arslan, "Comprehensive Big O Notation Guide," 5 4 2021. [Online]. Available: https://www.sahinarslan.tech/posts/comprehensive-big-o-notation-guide-in-plain-english-using-javascript. [Accessed 1 8 2023].
- [2] 	"Difference between Binary Search Tree and AVL Tree," [Online]. Available: https://www.geeksforgeeks.org/difference-between-binary-search-tree-and-avl-tree/. [Accessed 1 8 2023].
- [3] 	thatascrience, "The Ultimate Guide to Comments and Docstrings in Python," 2 1 2022. [Online]. Available: https://thatascience.com/learn-python/comments-and-docstrings-in-python/ . [Accessed 1 8 2023].
- [4] 	A. Raj, "Balanced Binary Tree in Python," 11 2 2021. [Online]. Available: https://www.askpython.com/python/examples/balanced-binary-tree. [Accessed 1 8 2023].
- [5] 	freeCodeCamp, "Binary Search Trees: BST Explained with Examples," 16 11 2019. [Online]. Available: https://www.freecodecamp.org/news/binary-search-trees-bst-explained-with-examples/. [Accessed 1 8 2023].


