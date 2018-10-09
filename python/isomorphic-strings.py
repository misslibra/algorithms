# -*- coding: utf-8 -*-

"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length
"""
from collections import defaultdict


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        >>> s, t = "egg", "add"
        >>> judge = Solution()
        >>> judge.isIsomorphic(s, t)
        True
        >>> s, t = "foo", "bar"
        >>> judge.isIsomorphic(s, t)
        False
        >>> s, t = "paper", "title"
        >>> judge.isIsomorphic(s, t)
        True
        """
        s_c = defaultdict(list)
        t_c = defaultdict(list)

        for k, i in enumerate(s):
            s_c[i].append(k)

        for k, i in enumerate(t):
            t_c[i].append(k)

        s_c_values = list(s_c.values())
        t_c_values = list(t_c.values())
        return sorted(s_c_values) == sorted(t_c_values)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
