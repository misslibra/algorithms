# -*- coding: utf-8 -*-

"""
Given an array consisting of n integers, find the contiguous subarray of given
length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

"""


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float

        连续，n项和,滑动窗口算法
        先算出前k项和
        然后滑动

        >>> test1, k = [1,12,-5,-6,50,3], 4
        >>> s = Solution()
        >>> s.findMaxAverage(test1, k)
        12.75
        """
        l = len(nums)
        max_ = sum_ = sum(nums[:k])
        flag = nums[0]
        for i in range(k, l):
            sum_ += nums[i] - flag
            flag = nums[i - k + 1]
            max_ = max(sum_, max_)
        return max_ / k


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
