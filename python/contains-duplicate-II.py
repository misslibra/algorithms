# -*- coding: utf-8 -*-

"""
Given an array of integers and an integer k, find out whether there are two distinct indices
i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        >>> nums, k = [1,2,3,1], 3
        >>> s = Solution()
        >>> s.containsNearbyDuplicate(nums, k)
        True
        >>> nums, k = [1,0,1,1], 1
        >>> s.containsNearbyDuplicate(nums, k)
        True
        >>> nums, k = [1, 2, 3, 1, 2, 3], 2
        >>> s.containsNearbyDuplicate(nums, k)
        False
        """
        l = len(nums)
        if l < 2:
            return False
        nums_map = {}
        for i in range(l):
            if nums[i] not in nums_map:  # value maybe zero
                nums_map[nums[i]] = i
            else:
                if i - nums_map[nums[i]] <= k:
                    return True
                else:
                    nums_map[nums[i]] = i
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
