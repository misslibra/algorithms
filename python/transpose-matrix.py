# -*- coding: utf-8 -*-

"""
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal,
switching the row and column indices of the matrix.


Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Note:

  1. 1 <= A.length <= 1000
  2. 1 <= A[0].length <= 1000

"""


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]

        >>> test1 = [[1,2,3],[4,5,6],[7,8,9]]
        >>> test2 = [[1,2,3],[4,5,6]]
        >>> s = Solution()
        >>> s.transpose(test1)
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        >>> s.transpose(test2)
        [[1, 4], [2, 5], [3, 6]]
        """
        r = []
        for i in zip(*A):
            r.append(list(i))
        return r


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
