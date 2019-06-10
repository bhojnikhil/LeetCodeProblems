# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[0]     
        self.travel(root,res)
        return res[0]
    
    def travel(self,root,res):
        if root is None:
            return 0
        left=self.travel(root.left,res)
        right=self.travel(root.right,res)
        res[0]+=abs(left-right)
        return left+right+root.val
