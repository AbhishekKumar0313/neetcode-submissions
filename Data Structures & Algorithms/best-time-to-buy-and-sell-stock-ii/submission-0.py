class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=sell=prices[0]
        profit=0
        for i in range(len(prices)):
            print(buy,sell,profit,i)
            if sell>prices[i]:
                profit+=sell-buy
                buy=sell=prices[i]
            else:
                sell=prices[i]
        return profit+sell-buy   
