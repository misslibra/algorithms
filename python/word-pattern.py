# -*- coding: utf-8 -*-

from collections import defaultdict


class Solution:
    def wordPattern(self, pattern, str_):
        """
        :type pattern: str
        :type str: str
        :rtype: bool

        >>> pattern1 , str1 = 'abba', 'dog cat cat dog'
        >>> pattern2 , str2 = 'abba', 'dog cat cat fish'
        >>> pattern3 , str3 = 'aaaa', 'dog cat cat dog'
        >>> pattern4 , str4 = 'abba', 'dog dog dog dog'
        >>> s = Solution()
        >>> s.wordPattern(pattern1, str1)
        True
        >>> s.wordPattern(pattern2, str2)
        False
        >>> s.wordPattern(pattern3, str3)
        False
        >>> s.wordPattern(pattern4, str4)
        False
        """
        pattern_map = defaultdict(set)
        for i in range(len(pattern)):
            pattern_map[pattern[i]].add(i)
        words = str_.split()

        if len(pattern) > len(words):
            return False

        words_map = defaultdict(set)
        for i in range(len(words)):
            words_map[words[i]].add(i)

        words_values = words_map.values()
        pattern_values = pattern_map.values()

        for i in words_values:
            if i not in pattern_values:
                return False
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
