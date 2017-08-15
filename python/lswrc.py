#!/usr/bin/env python
# encoding: utf-8
# author: cappyclearl


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) is 0:
            return len(s)
        # 字符之前出现的位置
        char_position = dict()
        # s[i-1]为末尾的最长无重复子串长度
        pre_arr = []
        for i, _ in enumerate(s):
            last_post_of_char = char_position.get(s[i])
            # 第一次出现当前字符
            if last_post_of_char is None:
                pre_arr.append(1 if i == 0 else pre_arr[i - 1] + 1)
                char_position[s[i]] = i
            else:
                # 不是第一次出现，统计前一个字符的lswrc长度
                a_pos = last_post_of_char + 1
                un_repeat_len = pre_arr[i - 1]
                b_pos = i - un_repeat_len
                if a_pos >= b_pos:
                    # 当前位置的lswrc
                    pre_arr.append(i - a_pos + 1)
                else:
                    pre_arr.append(i - b_pos + 1)
                # 更新当前字符位置，之前的不再记录
                char_position[s[i]] = i
        return max(pre_arr)


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('bbbbbb') == 1
    assert s.lengthOfLongestSubstring('') == 0
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('pwwkew') == 3
