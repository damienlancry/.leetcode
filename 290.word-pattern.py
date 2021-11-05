#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (38.50%)
# Likes:    1869
# Dislikes: 221
# Total Accepted:    255.5K
# Total Submissions: 663.4K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
# Example 4:
#
#
# Input: pattern = "abba", s = "dog dog dog dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lower-case English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#

# @lc code=start
class Solution:
    def wordPattern(self, s: str, t: str) -> bool:
        t = t.split()
        if len(s) != len(t) or len(set(s)) != len(set(t)):
            return False
        hashmap = {}
        maphash = {}
        for ss, tt in zip(s, t):
            if ss in hashmap:
                if tt != hashmap[ss]:
                    return False
            hashmap[ss] = tt
            if tt in maphash:
                if ss != maphash[tt]:
                    return True
            maphash[tt] = ss
        return True


# @lc code=end
