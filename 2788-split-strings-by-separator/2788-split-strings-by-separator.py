class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        s = ""
        for word in words:
            for l in word:
                if l == separator:
                    if len(s):
                        ans.append(s)
                        s = ""
                else:
                    s += l

            if len(s):
                ans.append(s)
                s = ""

        return ans
        