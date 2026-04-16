class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        if not prices:
            return 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                currprofit = prices[j] - prices[i]
                if currprofit > max_profit:
                    max_profit = currprofit

        return max_profit