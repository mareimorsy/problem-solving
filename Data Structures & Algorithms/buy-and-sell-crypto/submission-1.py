class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for i in prices:
            if i - min_price > max_profit:
                max_profit = i - min_price
            if i < min_price:
                min_price = i
        return max_profit