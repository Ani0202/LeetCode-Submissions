class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        def isValid(s):
            if m % s != 0 or n % s != 0:
                return False
            m1 = m // s
            n1 = n // s
            return str1 == m1 * str1[:s] and str2 == n1 * str1[:s]

        for i in range(min(m, n), 0, -1):
            if isValid(i):
                return str1[:i]

        return ""
