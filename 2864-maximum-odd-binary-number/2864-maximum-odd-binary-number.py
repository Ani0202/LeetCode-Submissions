class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        c = 0
        for i in s:
            if i == "1":
                c += 1
        return (c - 1) * "1" + (n - c) * "0" + "1"
