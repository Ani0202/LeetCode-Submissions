from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hmap = dict()
        for word in wordList:
            hmap[word] = False

        if endWord not in hmap:
            return 0

        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, count = queue.popleft()
            for i in range(len(word)):
                for j in range(26):
                    newWord = word[:i] + chr(j + 97) + word[i + 1 :]
                    if newWord in hmap:
                        if newWord == endWord:
                            return count + 1
                        if hmap[newWord] is False:
                            queue.append((newWord, count + 1))
                            hmap[newWord] = True

        return 0
