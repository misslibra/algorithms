# -*- coding: utf-8 -*-
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

"""

from collections import Counter


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> nums = [2,2,1]
        >>> s = Solution()
        >>> s.singleNumber(nums)
        1
        >>> nums =  [4,1,2,1,2]
        >>> s.singleNumber(nums)
        4
        """
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k
        # 这种是不聪明的
        # 聪明的是下面这种
        # 取原数据集的集合的值乘以2，刚好会比原数据集多出不重复整数的值
        # return sum(set(nums)) * 2  - sum(nums)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
