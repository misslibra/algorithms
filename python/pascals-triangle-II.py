# -*- coding: utf-8 -*-

"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
Example:

Input: 3
Output: [1,3,3,1]
Follow up:
Could you optimize your algorithm to use only O(k) extra space?
构造杨辉三角
"""


class Solution:
    def genRow(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(1, numRows + 2):
            if i <= 2:
                result = [1 for i in range(i)]
                continue
            current_line = []
            for j in range(i):
                if j == 0 or j == (i - 1):
                    current_line.append(1)
                else:
                    tmp = result[j] + result[j - 1]
                    current_line.append(tmp)
            result = current_line
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.getRow(1))
