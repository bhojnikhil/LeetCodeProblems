class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0 
        
        volume, left, right = 0, 0, len(height) - 1
        # Global Maximums for water 
        left_container, right_container = height[left], height[right]
        
        while left < right:
            left_container, right_container = max(left_container, height[left]), max(right_container, height[right])
            
            if left_container <= right_container:
                volume += left_container - height[left]
                left += 1
            else:
                volume += right_container  - height[right]
                right -= 1
                
        return volume
        

        #On3 Solution
    
        res=0
        s=len(height)
        
        for i in range(1,s-1):
            maxleft=maxright=0
            for j in range(i,0,-1):
                maxleft=max(maxleft,height[j])
            for j in range(i):
                if j<s:
                    maxright=max(maxright,height[j])
            res+=min(maxleft,maxright)-height[i]
        return res