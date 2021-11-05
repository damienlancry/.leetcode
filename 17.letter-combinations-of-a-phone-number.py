#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        hashmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        acc = [v for v in hashmap[digits[0]]]
        for i in range(1, len(digits)):
            next = []
            for val in list(hashmap[digits[i]]):
                for a in acc:
                    next.append(a + val)
            acc = next[:]
        return acc

        # def helper(digits, index, acc):
        #     if index == len(digits):
        #         return acc
        #     if index == len(digits) - 1:
        #         for val in hashmap[digits[index]]:
        #             acc = [a + [val] for a in acc]
        #         acc +=
        #     ans = []
        #     for val in hashmap[digits[i]]:
        #         sub
        #         ans += [val] + self.letterCombinations(digits)
        # return helper(digits, 0, [])


# @lc code=end
