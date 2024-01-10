class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        c = 0
        for i in s:
            if i == letter:
                c += 1

        return (c*100)//n