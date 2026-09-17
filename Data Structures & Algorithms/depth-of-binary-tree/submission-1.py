# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def _maxDepth(node):
            if node is None:
                return 0
            if node.right is None and node.left is None:
                return 1
            return max(_maxDepth(node.right), _maxDepth(node.left)) + 1
        return _maxDepth(root)