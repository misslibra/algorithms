# -*- coding: utf-8 -*-

"""
Given n non-negative integers a1, a2, ..., an, where each represents
a point at coordinate (i, ai). n vertical lines are drawn such that
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the
container contains the most water.

Note: You may not slant the container and n is at least 2.

"""


class Solution:
    max_area = 0

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        >>> s = Solution()
        >>> s.maxArea([1, 2, 3, 2, 3, 1, 5, 3, 7])
        18
        """
        if len(height) == 2:
            return min(height) * 1

        left, right = 0, len(height) - 1  # index from 0, last index is len(height) - 1
        while True:
            if left >= right:
                break
            width = right - left
            tmp = width * min(height[left], height[right])
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1

            if tmp > self.max_area:
                self.max_area = tmp
        return self.max_area


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
