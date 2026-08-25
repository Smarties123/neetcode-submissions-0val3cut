class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max_difference = 0

        for R in range(1, len(prices)):
            print("one:", L, R, max_difference)
            if prices[R] < prices[L]:
                L = R
                print("two:", L, R, max_difference)
            elif prices[R] > prices[L]:
                print("three:", L, R, max_difference)
                difference = prices[R] - prices[L]
                max_difference = max(difference, max_difference)

                print("four:", L, R, max_difference)
            print("five:", L, R, max_difference)
        return max_difference