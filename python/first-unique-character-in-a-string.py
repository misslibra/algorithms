# -*- coding: utf-8 -*-

"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from collections import defaultdict


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int

        >>> s1 = ""
        >>> s2 = "leetcode"
        >>> s3 = "loveleetcode"
        >>> s = Solution()
        >>> s.firstUniqChar(s1)
        -1
        >>> s.firstUniqChar(s2)
        0
        >>> s.firstUniqChar(s3)
        2

        """
        counter = defaultdict(list)
        for i, v in enumerate(s):
            counter[v].append(i)
        mini_index = len(s)
        for i in counter.values():
            if len(i) == 1:
                mini_index = min(i[0], mini_index)
        if mini_index < len(s):
            return mini_index
        else:
            return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
