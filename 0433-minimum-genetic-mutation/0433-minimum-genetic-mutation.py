class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        queue = deque([(startGene, 0)])
        mutations = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while queue:
            curr, ans = queue.popleft()
            if curr == endGene:
                return ans
            for i, gene in enumerate(curr):
                for mutation in mutations[gene]:
                    nextMut = curr[:i] + mutation + curr[i + 1:]
                    if nextMut in bank:
                        queue.append((nextMut, ans + 1))
                        bank.remove(nextMut)
        return -1
