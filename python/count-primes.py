# -*- coding: utf-8 -*-

"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

import math


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int

        >>> s = Solution()
        >>> n = 10
        >>> s.countPrimes(n)
        4
        """

        if n < 2:
            return 0
        r = [1 for i in range(n)]
        r[0] = r[1] = 0
        for i in range(2, int(math.sqrt(n) + 1)):  # 减小上界
            if r[i] == 1:
                r[i * i:n:i] = [0] * len(r[i * i:n:i])
        return sum(r)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
