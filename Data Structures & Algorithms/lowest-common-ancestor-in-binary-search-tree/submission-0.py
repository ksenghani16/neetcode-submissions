# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.solve(root,p,q)
    def solve(self,node,p,q):
        if not node:
            return None
        if node==p or node==q:
            return node
        left=self.solve(node.left,p,q)
        right=self.solve(node.right,p,q)
        if left==None:
            return right
        elif right==None:
            return left
        elif right==None and left==None:
            return None
        return node

        