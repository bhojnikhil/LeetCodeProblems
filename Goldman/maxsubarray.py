#BRUTE FORCE
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        for i in range(len(nums) + 1):  
            for j in range(i + 1, len(nums) + 1):   
                res.append(sum(nums[i:j]));
        return max(res)