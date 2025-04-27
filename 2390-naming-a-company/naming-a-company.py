class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        firstLetter = defaultdict(set)
        for idea in ideas:
            firstLetter[idea[0]].add(idea[1:])

        values = list(firstLetter.values())
        n = len(values)
        ans = 0
        for i in range(n):
            setA = values[i]
            for j in range(i + 1, n):
                setB = values[j]
                k = len(setA.intersection(setB))
                ans += 2 * (len(setA) - k) * (len(setB) - k)

        return ans
