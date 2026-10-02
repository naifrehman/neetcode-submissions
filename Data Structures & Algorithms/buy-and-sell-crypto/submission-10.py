class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 2 ptr problem

        """
        - need to return a profit 
        - profit must be 0 or > 
        - must iterate from left to right
        - need to return max profit 
        - left ptr focuses on buying the crypto first
        - right ptr focuses on selling
        """

        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                maxProfit = max(profit, maxProfit)

            right += 1

        return maxProfit
                


        