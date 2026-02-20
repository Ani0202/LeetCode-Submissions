class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        i = 0
        j = 0
        count = 0
        parts = []
        while j < len(s):
            if s[j] == "1":
                count += 1
            else:
                count -= 1

            if count == 0:
                parts.append("1" + self.makeLargestSpecial(s[i + 1 : j]) + "0")
                i = j + 1

            j += 1

        return "".join(sorted(parts, reverse=True))
