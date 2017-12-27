#!/usr/bin/env python3
# encoding: utf-8
# Author: Pyclearl

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        position = 0
        try:
            position = nums.index(target)
        except ValueError as e:
            l = len(nums)
            for i in range(l):
                if target < nums[i]:
                    position =  i
                    break
                else:
                    continue
            if target > nums[l-1]:
                position = l
        return position
