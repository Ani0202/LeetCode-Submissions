class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        self.ans = ""
        numSet = set(nums)
        temp = ""
        self.findUniqueStr(numSet, temp, n)
        return self.ans

    def findUniqueStr(self, numSet, temp, n):
        if len(temp) == n:
            if temp not in numSet:
                self.ans = temp
                return True
            else:
                return False

        for i in ["0", "1"]:
            temp += i
            if self.findUniqueStr(numSet, temp, n):
                return True
            temp = temp[:-1]

        return False
