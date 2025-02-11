class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        n = len(queries[0])
        for query in queries:
            for diction in dictionary:
                chn = 0
                for i in range(n):
                    if query[i] != diction[i]:
                        chn += 1
                    if chn > 2:
                        break

                if chn <= 2:
                    ans.append(query)
                    break

        return ans
