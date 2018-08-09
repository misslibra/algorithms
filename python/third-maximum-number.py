# -*- coding: utf-8 -*-

"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> test1 = [3, 2, 1]
        >>> test2 = [1, 2]
        >>> test3 = [2, 2, 3, 1]
        >>> test4 = [1, 1, 2]
        >>> s = Solution()
        >>> s.thirdMax(test1)
        1
        >>> s.thirdMax(test2)
        2
        >>> s.thirdMax(test3)
        1
        >>> s.thirdMax(test4)
        2
        """
        l = len(nums)
        result = []
        for i in range(0, l):
            if len(result) < 3:
                if nums[i] not in result:
                    result.append(nums[i])
            elif nums[i] not in result:
                result.append(nums[i])
                print(result)
                result.sort()
                result = result[1:]
        result.sort()
        if len(set(nums)) < 3 or l < 3:
            return max(nums)
        return result[0]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
