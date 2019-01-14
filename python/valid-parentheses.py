# -*- coding: utf-8 -*-

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool


        >>> s = Solution()
        >>> s.isValid("()[]{}")
        True
        >>> s.isValid("()")
        True
        >>> s.isValid("(]")
        False
        >>> s.isValid("([)]")
        False
        >>> s.isValid("{[]}")
        True
        """
        stack = []
        character_map = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if character_map.get(stack[-1]) == i:
                    stack.pop()
                else:
                    stack.append(i)
        return not len(stack)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)






