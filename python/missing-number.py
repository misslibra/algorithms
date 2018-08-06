# -*- coding: utf-8 -*-

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> test1 = [3, 0, 1]
        >>> test2 = [9,6,4,2,3,5,7,0,1]
        >>> test3 = [0]
        >>> s = Solution()
        >>> s.missingNumber(test1)
        2
        >>> s.missingNumber(test2)
        8
        >>> s.missingNumber(test3)
        1

        """
        l = len(nums)
        current_value = sum(nums)
        target_value = sum(i for i in range(l + 1))
        return target_value - current_value


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
