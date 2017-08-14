#!/usr/bin/env python
# encoding: utf-8
# author: cappyclearl
# TODO have bug


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_position = dict()
        pre_arr = []
        for i, _ in enumerate(s):
            last_post_of_char = char_position.get(s[i])
            if not last_post_of_char:
                pre_arr.append(1 if i == 0 else pre_arr[i - 1] + 1)
                char_position[s[i]] = i
            else:
                a_pos = last_post_of_char + 1
                un_repeat_len = pre_arr[i - 1]
                b_pos = i - un_repeat_len
                if a_pos >= b_pos:
                    pre_arr.append(i - a_pos + 1)
                else:
                    pre_arr.append(i - b_pos + 1)
                char_position[s[i]] = i
        maxlen = max(pre_arr)
        return maxlen


if __name__ == '__main__':
    pass
