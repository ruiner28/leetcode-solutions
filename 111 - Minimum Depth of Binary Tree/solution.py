# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif root.left == None and root.right ==None:
            return 1
        elif root.left ==None:
            return 1 + self.minDepth(root.right)
        elif root.right ==None:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
''' 
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth    
'''