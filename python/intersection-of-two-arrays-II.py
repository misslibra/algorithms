#!/usr/bin/env python
# encoding: utf-8

"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        >>> nums1, nums2 = [1, 2, 2, 1], [2, 2]
        >>> s = Solution()
        >>> s.intersect(nums1, nums2)
        [2, 2]
        """
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        set1 = set(nums1)
        set2 = set(nums2)
        inter = set1 & set2
        r = []
        for i in inter:
            for j in range(min(counter1[i], counter2[i])):
                r.append(i)
        return r


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
