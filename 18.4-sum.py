#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # seen = set()
        # ans = set()
        # for a in range(len(nums) - 2):
        #     for b in range(a + 1, len(nums) - 1):
        #         for c in range(b + 1, len(nums)):
        #             sum = nums[a] + nums[b] + nums[c]
        #             remain = target - sum
        #             if remain in seen:
        #                 numsa, numsb, numsc, numsd = sorted((nums[a], nums[b], nums[c], remain))
        #                 ans.add((numsa, numsb, numsc, numsd))
        #     seen.add(nums[a])
        # return ans
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                l, r = j + 1, n - 1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        print((nums[i], nums[j], nums[l], nums[r]))
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return ans


# @lc code=end
