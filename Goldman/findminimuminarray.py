class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo=0
        hi=len(nums)-1
        while(lo<hi):
            mid=(lo+hi)/2
            if(nums[mid]<nums[hi]):
                hi=mid
            else:
                lo=mid+1
        return nums[lo]