class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0 , 1
        res = 0 
        n = len(prices)
        while right < n:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                res = max(res,profit)
            
            else:
                left = right
        
            right +=1
        
        return res