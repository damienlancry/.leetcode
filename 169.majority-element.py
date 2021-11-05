#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                major = num
                count = 1
            elif major == num:
                count += 1
            else:
                count -= 1
        return major
        #  nums.sort()
        # return nums[len(nums) // 2]
        # majority_element = prev_element = nums[0]
        # majority_frequency = prev_frequency = 1

        # for current_element in nums[1:]:
        #     print(current_element)
        #     if current_element == prev_element:
        #         prev_frequency += 1
        #     else:
        #         print("khey")
        #         if prev_frequency > majority_frequency:
        #             majority_element = prev_element
        #             majority_frequency = prev_frequency
        #         prev_frequency = 1
        #         prev_element = current_element
        # if prev_frequency > majority_frequency:
        #     majority_element = prev_element
        #     majority_frequency = prev_frequency

        # return majority_element

        #         prev_element = current_element
        #         prev_frequency = 1

        # def divide_and_conquer(nums):
        #     if len(nums) == 1:
        #         return set(nums[0])
        #     if len()
        # def conquer(left, right):
        #     if len(left) == len(right) == 1:
        #         if left[0] == right[0]:
        #             return set(nums[0])
        #     if len(left)
        # n = len(nums)
        # left = nums[: n // 2 + 1]
        # right = nums[n // 2 + 1 :]
        # left_unique = set(left)
        # right_unique = set(right)
        # if len(left_unique) == 1:
        #     return left[0]
        # if len(right_unique) == 1:
        #     return right[0]
        # elif
        # print(set(nums[: n // 2 + 1]).intersection(nums[n // 2 + 1 :]))
        # (majority_element,) = set(nums[: n // 2 + 1]).intersection(nums[n // 2 + 1 :])
        # return majority_element


#        n = len(nums)
#        if n == 1:
#            return set(nums)
#        if n == 2:
#            return set(nums)
#        if n >= 3:
#            left_majority_element = self.majorityElement(nums[: n // 2 + 1])
#            right_majority_element = self.majorityElement(nums[n // 2 + 1 :])
#            print(left_majority_element)
#            print(right_majority_element)
#            (majority_element,) = set(left_majority_element).intersection(right_majority_element)
#            return majority_element


# @lc code=end
