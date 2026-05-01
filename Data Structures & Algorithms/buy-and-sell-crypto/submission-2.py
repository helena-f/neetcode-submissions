class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if not prices:
            return 0

        l,r = 0, 1

        while r < len(prices):
            curr = prices[r] - prices[l]
            if curr < 0:
                l = r
            
            if curr > max_profit:
                max_profit = curr
            
            r += 1

        return max_profit