# -*- coding: utf-8 -*-

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        >>> s = Solution()
        >>> s.isPalindrome(121)
        True
        >>> s.isPalindrome(-121)
        False
        >>> s.isPalindrome(10)
        False
        """
        s = str(x)
        if len(s) < 2 or len(set(s)) == 1:
            return True

        if s[0] != s[-1]:
            return False

        l = list(s)
        l.reverse()
        r = ''.join(l)
        if s == r:
            return True
        else:
            return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
