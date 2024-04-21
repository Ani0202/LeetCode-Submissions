class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = "0"
        for i in range(len(number)):
            if number[i] == digit:
                ans = max(ans, number[:i] + number[i + 1 :])

        return ans
