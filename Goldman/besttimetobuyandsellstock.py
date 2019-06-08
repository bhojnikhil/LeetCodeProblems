#Brute Force
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                if(profit>maxprofit):
                    maxprofit=profit
        return maxprofit

#one Pass
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit=0
        minprice=9999999
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            elif(prices[i]-minprice>maxprofit):
                maxprofit=prices[i]-minprice
        return maxprofit