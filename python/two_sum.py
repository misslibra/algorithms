#!/usr/bin/env python3
# encoding: utf-8
# author: cappyclearl

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype List[int]
        """
        for i, n in enumerate(nums):
            try:
                # 求n的补在nums中是否存在, 存在就返回，可能越界
                index = nums.index(target - n)
                if index != i:
                    return [i, index]
            except ValueError as e:
                pass
if __name__ == '__main__':
    pass



