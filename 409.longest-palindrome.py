#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter

        counter = Counter(s)
        print(counter)
        maxlen = 0
        oddcount = 0
        for v in counter.values():
            div, mod = v // 2, v % 2
            if oddcount == 0 and mod == 1:
                oddcount = 1
            maxlen += div * 2
        return maxlen + oddcount


# @lc code=end
