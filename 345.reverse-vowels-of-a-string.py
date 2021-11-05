#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        voyels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in voyels and s[j] in voyels:
                s[j], s[i] = s[i], s[j]
                i += 1
                j -= 1
            elif s[i] in voyels:
                j -= 1
            elif s[j] in voyels:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(s)


# @lc code=end
