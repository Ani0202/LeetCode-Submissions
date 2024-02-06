class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = float("inf")
        temp = startIndex
        n = len(words)
        while True:
            if words[temp] == target:
                print(ans, temp, startIndex)
                ans = min(ans, abs(temp-startIndex),n-abs(temp-startIndex))
            temp = (temp+1)%n
            if temp == startIndex:
                break
        return -1 if ans == float("inf") else ans
        