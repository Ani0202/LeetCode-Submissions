class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = {letter: 0 for word in words for letter in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for i in range(min_len):
                if w1[i] != w2[i]:
                    if w2[i] not in adj[w1[i]]:
                        adj[w1[i]].add(w2[i])
                        in_degree[w2[i]] += 1
                    break

        queue = deque([char for char in in_degree if in_degree[char] == 0])
        ans = []
        while queue:
            char = queue.popleft()
            ans.append(char)
            for neigh in adj[char]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        if len(ans) != len(in_degree):
            return ""

        return "".join(ans)
