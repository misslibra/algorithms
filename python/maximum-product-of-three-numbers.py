# -*- coding: utf-8 -*-

"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

"""


import functools
import operator


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        >>> test1 = [-4,-3,-2,-1,60]
        >>> s = Solution()
        >>> s.maximumProduct(test1)
        720


        nums.sort()
        three = nums[-3:]
        flag = 0
        for i in three:
            if i < 0:
                flag += 1
        if flag == 2:  # 负数为偶数个，选最小的两个和最大的那个数
            three[0:2] = nums[0:2]
            return functools.reduce(operator.imul, three)
        else:
            # 这里犯了个错，有可能最小的两个负数的值会非常大。
            mini = nums[0:2] + nums[-1:]
            return max(functools.reduce(operator.imul, mini), functools.reduce(operator.imul, three))
        """

        # 上面是第一次ac的答案，然后代码优化下就是下面这个了
        nums.sort()
        three = nums[-3:]
        mini = nums[0:2] + nums[-1:]
        return max(functools.reduce(operator.imul, mini), functools.reduce(operator.imul, three))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
