class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        l= 0
        while l < len(prices):

            for r in range(l+1,len(prices)):
                if prices[l] < prices[r]:
                    profit_new = prices[r] - prices[l]
                    if profit_new > profit:
                        profit = profit_new
            l = l + 1
        return profit

            
            

        