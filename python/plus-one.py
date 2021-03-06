# -*- coding: utf-8 -*-

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]


        >>> digits = [4,3,2,1]
        >>> digits2 = [1,9,9,9,9]
        >>> s = Solution()
        >>> s.plusOne(digits)
        [4, 3, 2, 2]
        >>> s.plusOne(digits2)
        [2, 0, 0, 0, 0]


        """
        s = int(''.join([str(i) for i in digits]))
        s += 1
        digits = [int(i) for i in str(s)]
        return digits


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
