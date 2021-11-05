#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def replaceOne(list):
            i = 0
            ans = []
            while i < len(list):
                if list[i] == 0:
                    list[i] = 1
                    ans.append(list[:])
                    list[i] = 0
                    i += 1
            return ans

        def replaceOneZero(listlists):
            listlistlist = [replaceOne(list) for list in listlists]
            listlist = [list for listlist in listlistlist for list in listlist]
            return listlist

        def combination(n, maxbits):
            if n > maxbits:
                return []
            if n == 0:
                return [[0] * maxbits]
            return replaceOneZero(combination(n - 1, maxbits))

        def convertListStr(list, max):
            hour = sum([2 ** i for i, n in enumerate(list) if n == 1])
            if hour > max:
                return ""
            return hour

        def convertString(listlist, max):
            liststr = [convertListStr(list, max) for list in listlist]
            return [str for str in liststr if str != ""]

        ans = []
        for i in range(turnedOn + 1):
            turnedOnHours = turnedOn - i
            turnedOnMinutes = i
            possibleHours = convertString(combination(turnedOnHours, 4), 11)
            possibleMinutes = convertString(combination(turnedOnMinutes, 6), 60)
            for hour in possibleHours:
                for minute in possibleMinutes:
                    hourstr = str(hour)
                    if minute > 9:
                        minutestr = str(minute)
                    else:
                        minutestr = f"0{minute}"
                    ans.append(f"{hourstr}:{minutestr}")
        return ans


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    ans = solution.readBinaryWatch(9)
