# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr):
            
            if not node:
                return 0 
            left = dfs(node.left, max(curr, node.val))    
            right = dfs(node.right, max(curr, node.val))  
            ans = left + right              
            if node.val >= curr:
                ans += 1
            return ans
        return dfs(root, float('-inf'))    
  