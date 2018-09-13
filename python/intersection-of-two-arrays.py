#!/usr/bin/env python
# encoding: utf-8

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
"""


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        >>> nums1, nums2 = [1, 2, 2, 1],[2, 2]
        >>> s = Solution()
        >>> s.intersection(nums1, nums2)
        [2]
        >>> nums1, nums2 = [4, 9, 5],[9, 4, 9, 8, 4]
        >>> s.intersection(nums1, nums2)
        [9, 4]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        r = set1 & set2
        return list(r)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
