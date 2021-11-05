#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countmag = dict()
        for c in magazine:
            if c in countmag:
                countmag[c] += 1
            else:
                countmag[c] = 1
        print(countmag)
        for c in ransomNote:
            if c in countmag:
                countmag[c] -= 1
            else:
                return False
        print(countmag)
        return all([v >= 0 for v in countmag.values()])


# @lc code=end
