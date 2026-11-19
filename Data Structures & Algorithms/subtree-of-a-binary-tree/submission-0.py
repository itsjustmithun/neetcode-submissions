# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
# i think its mostly bfs
# serach each level till the node of root and subRoot matches
# if doesnt match, return false
# if it does match, their is a possibility the subroot exists
# now take the node where both trees matches and start comparing them via recursive method

        if not root:
            return False
        if not subRoot:
            return True
        
        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode] ):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)) 
            
        return False
        