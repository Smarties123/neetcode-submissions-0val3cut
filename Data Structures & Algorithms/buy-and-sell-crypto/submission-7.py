class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_profit = 0

        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
            elif prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                max_profit = max(profit, max_profit)
        
        return max_profit
