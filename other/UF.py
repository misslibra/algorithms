#!/usr/bin/env python
# encoding: utf-8
# author: pyclearl


class Solution:
    def __init__(self, maps):
        self.maps = maps
        # 还没想清该怎么处理
        # self.count = len(maps) * 2
        # self._id = [i for i in range(self.count)]

    def union(self, p, q):
        pass

    def find(self, p):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def judge(self, s1, s2):
        str1 = s1.split()
        str2 = s2.split()
        for p, q in zip(str1, str2):
            if self.connected(p, q):
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    maps = {
        "movie": "film",
        "book": "note",
        "film": "show",
        "review": "rating"}
    s = Solution()
    assert s.judge("movie visible", "film show")
    assert not s.judge("book review", "movie rating")
