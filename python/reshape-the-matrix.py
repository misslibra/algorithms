# -*- coding: utf-8 -*-

"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with
different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing
the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing
order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

Example 1:
Input:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
Output:
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using
the previous list.
Example 2:
Input:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
Output:
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

"""


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]


        >>> s = Solution()
        >>> nums1 = [[1, 2], [3, 4]]
        >>> s.matrixReshape(nums1, 2, 4)
        [[1, 2], [3, 4]]
        >>> nums2 = [[1, 2], [3, 4]]
        >>> s.matrixReshape(nums1, 1, 4)
        [[1, 2, 3, 4]]
        """
        # 能够构成说明行号乘以列号的元素总数会是原本矩阵的元素总数
        r_l = len(nums)
        c_l = len(nums[0])
        if r_l * c_l != r * c:
            return nums

        elements = []
        for i in range(r_l):
            for j in range(c_l):
                elements.append(nums[i][j])
        result = []

        for i in range(0, r * c, c):  # 每次取c列个元素,所以步长设c
            result.append(elements[i:i + c])
        return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
