class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            tempStr = ""
            for i in range(len(s) - 1):
                tempStr += str((int(s[i]) + int(s[i + 1])) % 10)

            s = tempStr

        return s[0] == s[1]
