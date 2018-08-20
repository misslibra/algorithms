# -*- coding: utf-8 -*-

"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool


        >>> test1 = [4,2,3]
        >>> test2 = [4,2,1]
        >>> s = Solution()
        >>> s.checkPossibility(test1)
        True
        >>> s.checkPossibility(test2)
        False
        """
        l = len(nums)
        count = 0
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if i == 0:
                    nums[i] = nums[i + 1]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i + 1] = nums[i]
            if count > 1:
                return False
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
