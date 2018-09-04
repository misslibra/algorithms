# -*- coding: utf-8 -*-

"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from collections import Counter


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        >>> s, t =  "anagram", "nagaram"
        >>> check = Solution()
        >>> check.isAnagram(s,t)
        True
        """
        if len(s) == len(t):
            if set(s) == set(t):
                s_c = Counter(s)
                t_c = Counter(t)
                r = []
                for k in s_c.keys():
                    r.append(s_c[k] - t_c[k])
                return not any(r)  # 只要有个不为零，说明数目不匹配，返回False
            else:
                return False
        else:
            return False
        # 最简单的做法其实是
        # return sorted(s) == sroted(t)
        # 改进做法, 超过了50%
        # return set(s) == set(t) and sum(ord(i) for i in s) == sum(ord(i) for i in t)
        # 再快点,这个超过了80%的Python3写法
        # return bool(Counter(s) == Counter(t))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
