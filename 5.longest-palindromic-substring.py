#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest_start = 0
        longest_length = 1

        for i in range(n):
            left = i - 1
            right = i
            while right < n and s[right] == s[i]:
                right += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            # len(s[left+1: right-1]) = right - 1 - left
            if longest_length < right - left - 1:
                longest_length = right - left - 1
                longest_start = left + 1

        return s[longest_start : longest_start + longest_length]


# @lc code=end
