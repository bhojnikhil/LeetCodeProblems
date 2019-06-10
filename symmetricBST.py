# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def xyz(p,q):
            if p==None and q==None:
                return True
            if p!=None and q==None:
                return False
            if p==None and q!=None:
                return False
            return p.val==q.val and xyz(p.left,q.right) and xyz(p.right,q.left)
    
        return xyz(root,root)