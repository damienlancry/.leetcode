#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
def isanagram(s, t):
    hashmap = dict()
    for c in s:
        if c in hashmap:
            hashmap[c] += 1
        else:
            hashmap[c] = 1
    for c in t:
        if c not in hashmap:
            return False
        elif hashmap[c] == 0:
            return False
        else:
            hashmap[c] -= 1
    return all(v == 0 for v in hashmap.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for s in strs:
            t = "".join(sorted(s))
            if t in groups:
                groups[t].append(s)
            else:
                groups[t] = [s]
        return groups.values()


# @lc code=end
