# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """Return the preorder traversal of a tree given its root node.
        case:
        1. if root is None, return empty list
        2. recursive or iterative solution
        """
        def preorder(root,seq):
            if root is None:
                return seq
            seq.append(root.val)
            preorder(root.left,seq)
            preorder(root.right,seq)
            return seq
        
        prelist=  []
        return preorder(root,prelist)
