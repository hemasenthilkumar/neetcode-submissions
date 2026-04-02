class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = buy + 1 
        max_profit = 0
        while buy < sell and sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy + 1
            else:
                max_profit = max(max_profit, prices[sell]-prices[buy])
                sell += 1
            
        return max_profit
            