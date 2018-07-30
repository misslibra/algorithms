# -*- coding: utf-8 -*-

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。
        如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。

        >>> s1 = "babad"
        >>> s2 = "cbbd"
        >>> solution = Solution()
        >>> solution.longestPalindrome(s1)
        'bab'
        >>> solution.longestPalindrome(s2)
        'bb'
        """
        n = len(s)
        max_ = 0
        start = 0
        for i in range(n):
            if i - max_ >= 1 and s[i - max_ - 1: i + 1] == s[i - max_ - 1: i + 1][::-1]:
                start = i - max_ - 1
                max_ += 2
                continue
            if i - max_ >= 0 and s[i - max_: i + 1] == s[i - max_: i + 1][::-1]:
                start = i - max_
                max_ += 1
        return s[start: start + max_]

    def longestPalindromeManacher(self, s):
        """
        Manacher’s Algorithm用来解决最长回文子串
        >>> s1 = "babad"
        >>> s2 = "cbbd"
        >>> solution = Solution()
        >>> solution.longestPalindromeManacher(s1)
        'bab'
        >>> solution.longestPalindromeManacher(s2)
        'bb'
        """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
