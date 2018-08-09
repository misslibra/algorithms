# -*- coding: utf-8 -*-

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the
relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""


class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.


        >>> test1 = [0,1,0,3,12]
        >>> s = Solution()
        >>> s.moveZeroes(test1)
        >>> print(test1)
        [1, 3, 12, 0, 0]
        """
        l = len(nums)
        no_zero_cursor = 0
        for i in range(l):
            if nums[i]:
                nums[no_zero_cursor] = nums[i]
                no_zero_cursor += 1
        nums[no_zero_cursor:] = [0 for _ in range(l - no_zero_cursor)]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
