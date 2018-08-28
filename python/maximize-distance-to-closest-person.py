# -*- coding: utf-8 -*-

"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
"""


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int

        >>> seats = [1,0,0,0,1,0,1]
        >>> s = Solution()
        >>> s.maxDistToClosest(seats)
        2
        >>> seats = [1,0,0,0]
        >>> s.maxDistToClosest(seats)
        3
        """
        max_ = counter = 0
        for i, seat in enumerate(seats):
            if seat:
                if i - counter != 0:
                    counter = (counter // 2) + counter % 2
                max_ = max(counter, max_)
                counter = 0
            else:
                counter += 1
        max_ = max(counter, max_)
        return max_


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
