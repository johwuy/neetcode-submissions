# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isWithinBounds(node, lower_limit, upper_limit):
            if node is None:
                return True
            if not (lower_limit < node.val < upper_limit):
                return False
            return isWithinBounds(node.left, lower_limit, node.val) and isWithinBounds(node.right, node.val, upper_limit)
        return isWithinBounds(root, float("-inf"), float("inf"))