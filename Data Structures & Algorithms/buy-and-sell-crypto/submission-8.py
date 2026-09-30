class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # now solving using two pointers

        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            # if statement always ensures price @right is > then @ left
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)
            
            right += 1

        return maxProfit