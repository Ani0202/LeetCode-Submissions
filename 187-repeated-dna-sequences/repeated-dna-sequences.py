class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dnaSeq = dict()
        for i in range(len(s) - 9):
            dna = s[i : i + 10]
            dnaSeq[dna] = dnaSeq.get(dna, 0) + 1

        ans = []
        for k, v in dnaSeq.items():
            if v > 1:
                ans.append(k)

        return ans
