class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def find_palindrome(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            return s[i + 1 : j]

        ans = ""
        for i in range(n):
            odd_pal = find_palindrome(i, i)
            even_pal = find_palindrome(i, i + 1)
            if len(ans) < len(odd_pal):
                ans = odd_pal

            if len(ans) < len(even_pal):
                ans = even_pal

        return ans
