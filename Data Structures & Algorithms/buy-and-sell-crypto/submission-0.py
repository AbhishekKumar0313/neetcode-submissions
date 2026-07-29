class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,profit=prices[0],0
        for i in range(len(prices)):
            profit=max(profit,prices[i]-buy)
            buy=min(buy,prices[i])
        return profit