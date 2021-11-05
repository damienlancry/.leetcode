#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (59.02%)
# Likes:    2608
# Dislikes: 164
# Total Accepted:    818K
# Total Submissions: 1.4M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
        for c in t:
            hashmap[c] = hashmap.get(c, 0) - 1
        return set(hashmap.values()) == {0}


# @lc code=end
