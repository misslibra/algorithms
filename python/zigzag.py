#!/usr/bin/env python
# encoding: utf-8

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string text, int nRows);
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < numRows or numRows < 2:
            return s

        L = ['' for _ in range(numRows)]
        l = len(s)
        step = 2 * numRows - 2
        for j in range(numRows):
            if j == 0:
                for i in range(0, l, step):
                    L[j] += s[i]
            elif j == (numRows - 1):
                for i in range(j, l, step):
                    L[j] += s[i]
            else:
                for i in range(j, l, step):
                    L[j] += s[i]
                    # 与该层的正好处于两列中间的同一行下一元素的关系式
                    next_index = i + (numRows - 1 - j) * 2
                    if next_index < l:
                        L[j] += s[next_index]
        return ''.join(L)
