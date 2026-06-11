class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if (prices[l] < prices[r]):
                # Compute profit
                currP = prices[r] - prices[l]
                maxP = max(maxP, currP)
            else:
                # We only move L if R finds a value smaller
                l = r
            # Keep moving right pointer
            r += 1
        return maxP
