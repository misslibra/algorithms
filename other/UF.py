#!/usr/bin/env python
# encoding: utf-8
# author: pyclearl


class Solution:
    """
       字符串相似程度判断
       转化为连通性问题
    """
    def __init__(self, maps):
        self.maps = maps
        # 还没想清数据结构怎么处理
        # self.count = None
        # self._map = {}

    def union(self, p, q):
        p_map = self.find(p)
        q_map = self.find(q)
        if p_map == q_map:
            return

        for i in self._map.keys():
            if self._map[i] == p_map:
                self._map[i] = q_map
        self.count -= 1

    def find(self, p):
        return self._map[p]

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
        "review": "rating"
    }
    s = Solution()
    assert s.judge("movie visible", "film show")
    assert not s.judge("book review", "movie rating")
