class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxpro = 0
        for i in range(len(prices)):
            maxpro = max(prices[i] - minprice, maxpro)
            minprice = min(prices[i], minprice)

        return maxpro
