# -*- coding: utf-8 -*-

"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        遍历，累加，判断大小

        >>> test1 = [1,1,0,1,1,1]
        >>> s = Solution()
        >>> s.findMaxConsecutiveOnes(test1)
        3
        """
        sum_ = 0
        l = len(nums)
        max_ = 0
        for i in range(l):
            if nums[i] == 1:
                sum_ += 1
            else:
                sum_ = 0
            if sum_ > max_:
                max_ = sum_
        return max_


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
