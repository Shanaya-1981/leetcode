class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Initialize lowest price to first day's price
        lowest_price_so_far = prices[0]
        # Track the best profit seen so far
        maximum_profit = 0

        for price in range(len(prices)):
            current_price = prices[price]

            # Calculate profit if we sold today
            current_maximum_profit = current_price - lowest_price_so_far

            # Update max profit if today's profit is better
            if current_maximum_profit > maximum_profit:
                maximum_profit = current_maximum_profit

            # Update the lowest price if today is cheaper
            # This runs AFTER profit calculation to ensure buy before sell
            if current_price <= lowest_price_so_far:
                lowest_price_so_far = current_price

        return maximum_profit
