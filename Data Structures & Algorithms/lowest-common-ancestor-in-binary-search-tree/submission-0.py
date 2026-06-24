# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and root.val < q.val: 
            return root

        def dfs(node):
            
            if p.val < node.val and node.val < q.val:
                return node
            elif p.val < node.val and q.val < node.val: 
                return dfs(node.left)
            elif  p.val > node.val and q.val > node.val:
                return dfs(node.right)
            else: 
                return node
        return dfs(root)

            