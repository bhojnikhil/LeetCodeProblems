class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==0:
            return 1
        f=1
        s=2
        for i in range(3,n+1):
            t=f+s
            f=s
            s=t
        return s
        