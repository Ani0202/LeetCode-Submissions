class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = ""

        def findkthLexString(temp):
            nonlocal k, ans
            if len(temp) == n:
                k -= 1
                if k == 0:
                    ans = temp
                    return True

                return False

            for ele in "abc":
                if temp and temp[-1] == ele:
                    continue

                temp += ele
                if findkthLexString(temp):
                    return True

                temp = temp[:-1]

            return False

        findkthLexString("")
        return ans
