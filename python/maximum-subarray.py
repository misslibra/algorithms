# -*- coding: utf-8 -*-

"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        >>> s = Solution()
        >>> nums = [-2,1,-3,4,-1,2,1,-5,4]
        >>> s.maxSubArray(nums)
        6
        >>> nums1 = [-2,-1]
        >>> s.maxSubArray(nums1)
        -1
        >>> nums2 = [2,1]
        >>> s.maxSubArray(nums2)
        3


        Explanation: [4,-1,2,1] has the largest sum = 6.
        """
        # leetcode一个人的犀利解法。服气
        # for i in range(1, len(nums)):
        #    if nums[i-1] > 0:
        #        nums[i] += nums[i-1]
        # return max(nums)
        l = len(nums)
        if l == 1:
            return nums[0]
        sum_ = nums[0]
        max_ = nums[0]
        for i in range(1, l):
            sum_ = max(nums[i], sum_ + nums[i])
            max_ = max(sum_, max_)
        return max_


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
