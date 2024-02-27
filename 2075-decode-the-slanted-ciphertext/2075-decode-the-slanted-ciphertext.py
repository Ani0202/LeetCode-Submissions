class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        ans = []
        for i in range(cols):
            r, c = 0, i
            while r < rows and c < cols:
                ans.append(encodedText[r * cols + c])
                r += 1
                c += 1
        return "".join(i for i in ans).rstrip()
