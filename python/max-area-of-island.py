# -*- coding: utf-8 -*-
"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
(representing land) connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        >>> test1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                    [0,1,1,0,1,0,0,0,0,0,0,0,0],
                    [0,1,0,0,1,1,0,0,1,0,1,0,0],
                    [0,1,0,0,1,1,0,0,1,1,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,1,1,1,0,0,0],
                    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
        >>> test2 = [[0,0,0,0,0,0,0,0]]
        >>> s = Solution()
        >>> s.maxAreaOfIsland(test1)
        6
        >>> s.maxAreaOfIsland(test2)
        0

        """
        # 深度优先
        if len(grid) == 0:
            return 0
        h = len(grid)  # 高
        w = len(grid[0])  # 宽
        marked = set()
        max_area = 0
        for i in range(h):
            for j in range(w):
                # 如果是陆地，开始以该点为中心深度搜索，做过标记的不看了
                if grid[i][j] == 1 and (i, j) not in marked:
                    marked.add((i, j))
                    stack = [(i, j)]
                    area = 1
                    while stack:
                        top = stack.pop()
                        i, j = top[0], top[1]
                        # 看垂直的左边
                        if i > 0 and grid[i - 1][j] == 1 and (i - 1,
                                                              j) not in marked:
                            stack.append((i - 1, j))
                            marked.add((i - 1, j))
                            area += 1
                        # 看垂直的右边
                        if i < h - 1 and grid[i + 1][j] == 1 and (
                                i + 1, j) not in marked:
                            stack.append((i + 1, j))
                            marked.add((i + 1, j))
                            area += 1
                        # 看水平左边
                        if j > 0 and grid[i][j - 1] == 1 and (
                                i, j - 1) not in marked:
                            stack.append((i, j - 1))
                            marked.add((i, j - 1))
                            area += 1
                        # 看水平右边
                        if j < w - 1 and grid[i][j + 1] == 1 and (
                                i, j + 1) not in marked:
                            stack.append((i, j + 1))
                            marked.add((i, j + 1))
                            area += 1
                    max_area = max(area, max_area)
        return max_area


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
