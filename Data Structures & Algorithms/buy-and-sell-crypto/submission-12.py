class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_diff = 0

        for R in range(1, len(prices)):
            if prices[R] > prices[L]:
                diff = prices[R] - prices[L]
                if diff > max_diff:
                    max_diff = diff
            else:
                L = R
        
        return max_diff