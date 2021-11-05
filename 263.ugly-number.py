#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (41.68%)
# Likes:    773
# Dislikes: 793
# Total Accepted:    240.1K
# Total Submissions: 576.2K
# Testcase Example:  '6'
#
# An ugly number is a positive integer whose prime factors are limited to 2, 3,
# and 5.
#
# Given an integer n, return true if n is an ugly number.
#
#
# Example 1:
#
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
#
# Input: n = 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
#
#
# Example 3:
#
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
#
# Example 4:
#
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are
# limited to 2, 3, and 5.
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)
        return False


# @lc code=end
