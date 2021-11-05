#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        while s[len(s) - 1 - i] == " ":
            i += 1
        count = 0
        start_last_word = len(s) - 1 - i
        while start_last_word - count >= 0 and s[start_last_word - count] != " ":
            count += 1
        return count


# @lc code=end
