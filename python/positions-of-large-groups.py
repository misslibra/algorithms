# -*- coding: utf-8 -*-
"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.
We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]


Note:  1 <= S.length <= 1000
"""


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]

        >>> S = "abcdddeeeeaabbbcd"
        >>> s = Solution()
        >>> s.largeGroupPositions(S)
        [[3, 5], [6, 9], [12, 14]]
        """
        l = len(S)
        S = S + 'A'
        result = []
        cursor = S[0]
        counter = 0
        for i in range(l + 1):
            if S[i] == cursor:
                counter += 1
            else:
                if counter >= 3:
                    result.append([i - counter, i - 1])
                counter = 1
                cursor = S[i]
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
