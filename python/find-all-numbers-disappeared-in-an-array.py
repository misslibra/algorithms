# -*- coding: utf-8 -*-

"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]


        >>> test1 = [4, 3, 2, 7, 8, 2, 3, 1]
        >>> test2 = [1, 1]
        >>> s = Solution()
        >>> s.findDisappearedNumbers(test1)
        [5, 6]
        >>> s.findDisappearedNumbers(test2)
        [2]
        """
        # n = size of array
        end = len(nums)
        if end < 1:
            return []
        s = set(nums)
        result = []
        for i in range(1, end + 1):
            if i not in s:
                result.append(i)
        return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
