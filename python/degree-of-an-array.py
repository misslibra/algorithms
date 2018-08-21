# -*- coding: utf-8 -*-

"""
Given a non-empty array of non-negative integers nums, the degree of this array
is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
"""

from collections import Counter, defaultdict


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> test1 = [1,2,2,3,1,4,2]
        >>> test2 = [1, 2, 2, 3, 1]
        >>> s = Solution()
        >>> s.findShortestSubArray(test1)
        6
        >>> s.findShortestSubArray(test2)
        2
        """
        l = len(nums)
        min_ = l
        if l == 0:
            return 0
        else:
            count = Counter(nums)
            visited = defaultdict(list)
            degree = max(count.values())
            for i in range(l):
                visited[nums[i]].append(i)
            tmp = 0
            for i in count.keys():
                if count[i] == degree:  # if i element counter is degree, change
                    tmp = visited[i][-1] - visited[i][0] + 1
                    min_ = min(min_, tmp)
        return min_


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

