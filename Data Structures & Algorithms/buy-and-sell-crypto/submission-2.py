class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input: prices = [10, 1, 5, 6, 7, 1]
        #                   b  s
        # profit = s - b

        # Output: 6

        maxProfit = 0
        l, r = 0, 1 #left is buying, #right is selling

        while r < len(prices):
            # profitable ?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                # shift the l to the position of the r
                l = r
            # regardless 
            r +=1

        return maxProfit
        