from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        geneBank = set(bank)
        queue = deque()
        queue.append((startGene, 0))
        while queue:
            gene, count = queue.popleft()
            for i in range(8):
                for j in "ACGT":
                    newGene = gene[:i] + j + gene[i + 1 :]
                    if newGene in geneBank:
                        if newGene == endGene:
                            return count + 1

                        queue.append((newGene, count + 1))
                        geneBank.remove(newGene)

        return -1
