class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        selling_price = prices[0]
        j = 1
        current_profit = 0
        while j < len(prices):
            if prices[j] < buying_price:
                buying_price = prices[j]
                selling_price = prices[j]
            elif prices[j] > selling_price:
                selling_price = prices[j]
                if current_profit < selling_price - buying_price:
                    current_profit = selling_price - buying_price
            j += 1
        return current_profit

