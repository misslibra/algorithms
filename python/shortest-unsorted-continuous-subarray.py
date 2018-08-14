# -*- coding: utf-8 -*-

"""
Given an integer array, you need to find one continuous subarray that if you only sort
this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> s = Solution()
        >>> nums = [2, 6, 4, 8, 10, 9, 15]
        >>> s.findUnsortedSubarray(nums)
        5
        """
        s = nums[:]
        s.sort()
        if s == nums:
            return 0
        else:
            for i in range(len(s)):
                if s[i] - nums[i] != 0:
                    start = i
                    break
            for i in range(len(s) - 1, -1, -1):
                if s[i] - nums[i] != 0:
                    end = i
                    break
        # start end是index。。
        return (end - start + 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
