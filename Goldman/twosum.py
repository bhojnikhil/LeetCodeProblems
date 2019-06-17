class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        di={}
        for i in range(len(nums)):
            if target-nums[i] not in di:
                di[nums[i]]=i
            else:
                return [di[target-nums[i]],i]
