from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, count = queue.popleft()
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(j + 97) + word[i + 1 :]
                    if newWord in wordSet:
                        if newWord == endWord:
                            return count + 1

                        queue.append((newWord, count + 1))
                        wordSet.remove(newWord)

        return 0
