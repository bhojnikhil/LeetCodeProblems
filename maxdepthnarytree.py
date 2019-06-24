    def maxDepth(self,root):    
        res = 0
        if not root:
            return 0
        if root.children:
            for root in root.children:
                res =  max(res,self.maxDepth(root))
        return 1 + re