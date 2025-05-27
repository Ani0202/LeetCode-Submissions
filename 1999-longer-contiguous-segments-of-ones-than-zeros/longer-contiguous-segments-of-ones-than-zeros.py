class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zeros = 0
        currZeros = 0
        ones = 0
        currOnes = 0
        for i in s:
            if i == "1":
                currZeros = 0
                currOnes += 1
            else:
                currZeros += 1
                currOnes = 0

            ones = max(ones, currOnes)
            zeros = max(zeros, currZeros)

        return ones > zeros
