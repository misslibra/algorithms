#!/usr/bin/env python
# encoding: utf-8

"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int

        >>> cost = [10, 15, 20]
        >>> s = Solution()
        >>> s.minCostClimbingStairs(cost)
        15
        >>> cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
        >>> s.minCostClimbingStairs(cost)
        6
        """

        tmp1,tmp2 = cost[0], cost[1]
        total_cost = 0
        l = len(cost)
        for i in range(2, l + 1):   # becase exists top so l + 1 is top
            if i != l:
                total_cost = min(tmp1, tmp2) + cost[i]  # total_cost + cost[i-1]  cmp total_cost, total cost must be minimum
                tmp1 = tmp2
                tmp2 = total_cost
            else:
                total_cost = min(tmp1, tmp2)
        return total_cost

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
