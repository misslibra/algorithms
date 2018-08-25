#!/usr/bin/env python
# encoding: utf-8

"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.


Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

"""


class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> nums = [3, 6, 1, 0]
        >>> s=Solution()
        >>> s.dominantIndex(nums)
        1
        >>> nums = [1, 2, 3, 4]
        >>> s.dominantIndex(nums)
        -1
        """
        max_ = max(nums)
        index = nums.index(max_)
        nums.pop(index)
        if all(map(lambda x: (2*x) <= max_, nums)):
            return index
        else:
            return -1

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
