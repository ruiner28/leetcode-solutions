class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def transverse(node):
            if not node:
                return 0
            transverse(node.left)
            arr.append(node.val)
            transverse(node.right)

            return arr          
        transverse(root) 
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, (arr[i] - arr[i -1]))
        return min_diff    