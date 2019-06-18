# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if not root.left and root.right:
            return 1+self.minDepth(root.right)
        
        if not root.right and root.left:
            return 1+self.minDepth(root.left)
        
        left=1+self.minDepth(root.left)
        right=1+self.minDepth(root.right)
        
        return min(left,right)