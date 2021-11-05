#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        reversed = 0
        while x > reversed:
            reversed = 10 * reversed + x % 10
            x = x // 10
        return x == reversed or x == reversed // 10


# @lc code=end
