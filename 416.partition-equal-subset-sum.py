#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
def pprint(dp):
    print("\n".join(", ".join(str(i) for i in l) for l in dp))
    print()


class Solution:
    # brute force:O(2^n)
    # def canPartition(self, nums: List[int]) -> bool:
    #     s = sum(nums)
    #     if s % 2 == 1:
    #         return False
    #     s = s // 2
    #     return self.helper(nums, s, 0)

    # def helper(self, nums, j, i):
    #     if j == 0:
    #         return True
    #     if i == len(nums):
    #         return False
    #     if nums[i] <= j:
    #         if self.helper(nums, j - nums[i], i + 1):
    #             return True
    #     return self.helper(nums, j, i + 1)

    # dynamic programming: top down - memoization
    # def canPartition(self, nums: List[int]) -> bool:
    #     s = sum(nums)
    #     if s % 2 == 1:
    #         return False
    #     s = s // 2
    #     memo = [[None for _ in range(s + 1)] for _ in range(len(nums) + 1)]
    #     return self.helper(nums, s, 0, memo)

    # def helper(self, nums, j, i, memo):
    #     if memo[i][j] is None:
    #         if j == 0:
    #             memo[i][j] = True
    #             return True
    #         if i == len(nums):
    #             memo[i][j] = False
    #             return False
    #         if nums[i] <= j and self.helper(nums, j - nums[i], i + 1, memo):
    #             memo[i][j] = True
    #             return True
    #         memo[i][j] = self.helper(nums, j, i + 1, memo)
    #     return memo[i][j]

    # dynamic programming: bottom up - tabulation
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        s = s // 2
        n = len(nums)
        memo = [[False for _ in range(s + 1)] for _ in range(n)]
        for i in range(n):
            memo[i][0] = True
        for j in range(s + 1):
            memo[0][j] = nums[0] == j
        for i in range(1, n):
            for j in range(s + 1):
                if memo[i - 1][j]:
                    memo[i][j] = True
                    continue
                if j >= nums[i]:
                    memo[i][j] = memo[i - 1][j - nums[i]]
        return memo[n - 1][s]


# @lc code=end
