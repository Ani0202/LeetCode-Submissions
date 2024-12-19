class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            s = (0 if i < 0 else int(a[i])) + (0 if j < 0 else int(b[j])) + carry
            ans += str(s % 2)
            carry = s // 2
            i -= 1
            j -= 1

        return ans[::-1]
