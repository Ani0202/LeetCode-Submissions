class Solution:
    def minimumPushes(self, word: str) -> int:
        press = 0
        for i in range(len(word)):
            press += (i // 8) + 1

        return press
