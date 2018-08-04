# -*- coding: utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

低买高卖，数组是每天价格，卖必须先买，只允许一次买卖，要得到最大利润。
"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        >>> s = Solution()
        >>> test1 = [7,1,5,3,6,4]
        >>> test2 = [7,6,4,3,1]
        >>> s.maxProfit(test1)
        5
        >>> s.maxProfit(test2)
        0
        """
        # 这种解法是很自然的Python程序员做法
        # min_index = prices.index(min(prices))
        # max_value = max(prices[min_index:])
        # max_index = prices.index(max_value, min_index)
        # if min_index < max_index:
            # return prices[max_index] - prices[min_index]
        # else:
            # return 0

        # 这种做法是基于一个规律的，想像这些点是y轴的坐标点
        # 那么俩点间的距离可以由两点间包含的各个点两两之差的和构成
        # 于是最大的利润是距离最大的两点
        max_ = 0
        l = len(prices)
        tmp = 0
        for i in range(1, l):
            tmp += prices[i] - prices[i - 1]
            if tmp < 0:
                tmp = 0
            if max_ < tmp:
                max_ = tmp
        return max_


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
