# -*- coding: utf-8 -*-

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int


        >>> test1 = [3,2,3]
        >>> test2 = [2,2,1,1,1,2,2]
        >>> s = Solution()
        >>> s.majorityElement(test1)
        3
        >>> s.majorityElement(test2)
        2
        """
        # 遍历，增加一个辅助字典，以数字为key在相应位置
        temp = {}
        for i in nums:
            if not temp.get(i):
                temp[i] = 1
            else:
                temp[i] += 1
        max_ = 0
        elem = 0
        for k, v in temp.items():
            if v > max_:
                max_ = v
                elem = k
        return elem


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
