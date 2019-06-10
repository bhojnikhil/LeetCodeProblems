class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        #d=[]
        d = str(x)
        #num = x
        #while num > 0:
        #    d.append(num % 10)
        #    num = num/10
        for i in range(len(d)/2):
            j = len(d)-1-i
            if d[i] != d[j]:
                return False
        return True