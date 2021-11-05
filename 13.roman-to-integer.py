#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        sum = 0
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        hashmap = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        for i in range(len(s) - 1):
            if s[i + 1] in hashmap.get(s[i], []):
                sum -= values[s[i]]
            else:
                sum += values[s[i]]
        return sum + values[s[len(s) - 1]]


# @lc code=end
