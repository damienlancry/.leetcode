#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:

            if nums[p2] == val:
                p2 -= 1
                continue
            if nums[p1] == val:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1
                continue
            else:
                p1 += 1
        return p1 + 1 if p1 <= p2 else p2 + 1


# @lc code=end
