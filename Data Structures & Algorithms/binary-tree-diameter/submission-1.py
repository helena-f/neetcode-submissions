# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(node):
            nonlocal res
            # get the sum of the left and right max height to update res
            # node height gets added 1
            if not node:
                return 0 # zero height for no node

            left_height = dfs(node.left)
            right_height = dfs(node.right)
            d = left_height + right_height
            res = max(d, res)

            return max(left_height, right_height) + 1

        dfs(root)
        return res
        
