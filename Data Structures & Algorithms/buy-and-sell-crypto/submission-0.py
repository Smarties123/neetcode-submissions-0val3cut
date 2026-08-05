class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest_profit = 0
        L = 0  # index of the lowest price seen so far

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R  # update lowest price day

            profit = prices[R] - prices[L]
            if profit > highest_profit:
                highest_profit = profit

        return highest_profit

