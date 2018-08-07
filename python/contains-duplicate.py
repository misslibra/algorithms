# -*- coding: utf-8 -*-

"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool


        >>> test1 = [1,2,3,1]
        >>> test2 = [1,2,3,4]
        >>> test3 = [1,1,1,3,3,4,3,2,4,2]
        >>> s = Solution()
        >>> s.containsDuplicate(test1)
        True
        >>> s.containsDuplicate(test2)
        False
        >>> s.containsDuplicate(test3)
        True

        """
        # 这题对Python来说一句搞定,而且还符合直觉
        # return len(nums) == len(set(nums)):

        # 下面的还花了下脑子。。
        is_duplicate = False
        nums.sort()
        l = len(nums)
        for i in range(1, l):
            if nums[i - 1] == nums[i]:
                is_duplicate = True
        return is_duplicate


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
