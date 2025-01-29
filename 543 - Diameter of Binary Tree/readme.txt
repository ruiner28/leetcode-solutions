Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 

Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

Intuition
The problem requires finding the diameter of a binary tree, which is defined as the number of nodes along the longest path between any two nodes in the tree. Initially, consider traversing the tree recursively, calculating the length of the longest path passing through each node.

Approach
The approach involves a recursive depth-first traversal of the binary tree. At each node, calculate the length of the longest path passing through that node (which is the sum of the heights of its left and right subtrees). Keep track of the maximum diameter encountered so far.