class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_seen)
            min_seen = min(min_seen, price)

        return max_profit