class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            else:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            right += 1
        return max_profit