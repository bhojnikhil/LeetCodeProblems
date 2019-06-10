# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def ios(root,L):
            if root is not None:
                ios(root.left,L)
                L.append(root.val)
                ios(root.right,L)
            
        L=[]
        ios(root,L)
        newtree=TreeNode(L[0])
        dummy=newtree
        for i in range(1,len(L)):
            newtree.right=TreeNode(L[i])
            newtree=newtree.right
        return dummy
    