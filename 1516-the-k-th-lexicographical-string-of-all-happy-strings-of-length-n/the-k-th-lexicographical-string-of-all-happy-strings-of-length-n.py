class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happyStrings = []
        tempString = ""
        self.findStr(happyStrings, tempString, n)
        if len(happyStrings) < k:
            return ""
        return happyStrings[k - 1]

    def findStr(self, happyStrings, tempString, n):
        if len(tempString) == n:
            happyStrings.append(tempString)
            return

        for letter in ["a", "b", "c"]:
            if len(tempString) > 0 and tempString[-1] == letter:
                continue

            tempString += letter
            self.findStr(happyStrings, tempString, n)
            tempString = tempString[:-1]
