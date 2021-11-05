#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for num in nums:
            if num in seen:
                ans.append(num)
            else:
                seen.add(num)
        (other,) = set(range(1, len(nums) + 1)).difference(seen)
        ans.append(other)
        return ans


# @lc code=end
