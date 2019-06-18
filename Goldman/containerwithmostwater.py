class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea=0
        l=0
        r=len(height)-1
        while(l<r):
            maxarea=max(maxarea, min(height[l],height[r]) * (r-l))
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return maxarea
            
            
        #alternative 0(n2) solution!
            
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                maxarea=max(maxarea, min(height[i],height[j]) * (j-i))
        return maxarea