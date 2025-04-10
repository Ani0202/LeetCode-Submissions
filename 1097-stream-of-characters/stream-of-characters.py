class StreamChecker:

    def __init__(self, words: List[str]):
        self.suffs = dict()
        self.chars = ""
        for word in words:
            if word[-1] in self.suffs:
                self.suffs[word[-1]].append(word)
            else:
                self.suffs[word[-1]] = [word]

    def query(self, letter: str) -> bool:
        self.chars += letter
        if letter in self.suffs:
            for word in self.suffs[letter]:
                n = len(word)
                if n <= len(self.chars) and word == self.chars[-n:]:
                    return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)