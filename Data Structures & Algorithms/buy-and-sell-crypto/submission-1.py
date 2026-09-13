class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_sell = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            buy_price = prices[i]
            if best_sell - buy_price > max_profit:
                max_profit = best_sell - buy_price
            best_sell = max(best_sell, buy_price)
        return max_profit