# -*- coding: utf-8 -*-

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
构造杨辉三角
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(1, numRows + 1):
            if i <= 2:
                result.append([1 for i in range(i)])
                continue
            current_line = []
            for j in range(i):
                if j == 0 or j == (i - 1):
                    current_line.append(1)
                else:
                    print(result)
                    tmp = result[i - 2][j] + result[i - 2][j - 1]
                    current_line.append(tmp)
            result.append(current_line)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.generate(1))
