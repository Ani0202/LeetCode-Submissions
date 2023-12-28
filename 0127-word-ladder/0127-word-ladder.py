class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = defaultdict(int)
        for word in wordList:
            visited[word] = 1
        if endWord not in wordList:
            return 0
        queue = deque()
        queue.append([beginWord, 1])
        while queue:
            word, ans = queue.popleft()
            for ind in range(len(word)):
                for i in range(26):
                    nextWord = word[:ind] + chr(i+97) + word[ind+1:]
                    if nextWord != word and visited[nextWord]:
                        if nextWord == endWord:
                            return ans + 1
                        queue.append([nextWord, ans+1])
                        visited[nextWord] = 0

        return 0
        