class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)), reverse=num < 0)
        n = 0
        for i, c in enumerate(s):
            if c != "0":
                n = i
                break
        s[n], s[0] = s[0], s[n]
        return int("".join(s)) * (-1 if num < 0 else 1)
