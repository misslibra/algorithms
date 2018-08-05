# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

低买高卖，数组是每天价格，卖必须先买，允许多次买卖，要得到总利润。
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        >>> s = Solution()
        >>> test1 = [7,1,5,3,6,4]
        >>> s.maxProfit(test1)
        7
        >>> test2 = [1,2,3,4,5]
        >>> s.maxProfit(test2)
        4
        >>> test3 = [7,6,4,3,1]
        >>> s.maxProfit(test3)
        0
        """

        # 这种做法是基于一个规律的，想像这些点是y轴的坐标点
        # 那么俩点间的距离可以由两点间包含的各个点两两之差的和构成
        total = 0
        l = len(prices)
        for i in range(1,l):
            if prices[i-1] < prices[i]:
                total += prices[i] - prices[i-1]
        return total


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
