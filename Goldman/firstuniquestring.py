class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        maph = collections.Counter(s)
        i=0
        for x in s:
            if maph[x]==1:
                return i
            else:
                i+=1
        return -1