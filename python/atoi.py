#!/usr/bin/env python3
# encoding: utf-8
# author: cappyclearl


class Solution(object):
    r_min = -2147483648
    r_max = 2147483647

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r_int = 0
        sign = 1
        str = str.lstrip()
        if str.isdigit():
            return self.judgeRange(int(str))
        else:
            for i, c in enumerate(str):
                if i == 0:
                    if c == '-':
                        sign = -1
                        continue
                    if c == '+':
                        sign = 1
                        continue
                if c.isdigit():
                    # 一个数乘上所在位的权
                    r_int = r_int * 10 + int(c)
                else:
                    return self.judgeRange(sign* r_int)
            return self.judgeRange(sign* r_int)

    def judgeRange(self, result):
        if result > self.r_max:
            return self.r_max
        if result < self.r_min:
            return self.r_min
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('123') == 123
    assert s.myAtoi('-123') == -123
