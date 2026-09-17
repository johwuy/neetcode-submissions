# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _isSameTree(node_a, node_b):
            if node_a is None and node_b is None:
                return True

            if node_a is None or node_b is None:
                return False

            if node_a.val != node_b.val:
                return False
            return (
                _isSameTree(node_a.left, node_b.left)
                and _isSameTree(node_a.right, node_b.right)
            )
        return _isSameTree(p, q)