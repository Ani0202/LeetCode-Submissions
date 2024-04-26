class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = 0
        temp = 0
        vowels = "aeiou"
        i = 0
        j = 0
        while j < len(s):
            if s[j] in vowels:
                temp += 1

            if j - i + 1 > k:
                if s[i] in vowels:
                    temp -= 1
                i += 1

            ans = max(ans, temp)
            j += 1

        return ans
