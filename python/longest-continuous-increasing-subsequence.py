# -*- coding: utf-8 -*-

"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5],
its length is 3.
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1.
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> test1 = [2,2,2,2,2]
        >>> test2 = [1, 3, 5, 4, 7]
        >>> s = Solution()
        >>> s.findLengthOfLCIS(test1)
        1
        >>> s.findLengthOfLCIS(test2)
        3
        """
        l = len(nums)
        if l < 1:
            return 0
        current = 1
        max_ = 1
        tmp = nums[0]
        for i in range(1, l):
            if tmp < nums[i]:  # example2
                current += 1
                max_ = max(current, max_)
            else:
                current = 1
            tmp = nums[i]
        return max_


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
