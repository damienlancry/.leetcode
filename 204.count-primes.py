#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (32.36%)
# Likes:    2997
# Dislikes: 772
# Total Accepted:    466.1K
# Total Submissions: 1.4M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 5 * 10^6
#
#
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [0, 0] + [1] * (n - 2)
        for i in range(2, n):
            if sieve[i] == 1:
                for j in range(i * i, n, i):
                    sieve[j] = 0
        return sum(sieve)


# @lc code=end
