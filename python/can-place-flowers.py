# -*- coding: utf-8 -*-


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool

        >>> test1, n = [1,0,1,0,1,0,1], 1
        >>> s = Solution()
        >>> s.canPlaceFlowers(test1, n)
        False
        >>> test2, n = [1,0,1,0,1,0,1], 0
        >>> s.canPlaceFlowers(test1, n)
        True
        """
        if n == 0:
            return True
        # 统一不同情况
        a = [0] + flowerbed + [0]
        l = len(a)
        for i in range(1, l - 1):  # 首尾一定是0所以不需要判断
            if a[i - 1] == a[i] == a[i + 1] == 0:
                a[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
