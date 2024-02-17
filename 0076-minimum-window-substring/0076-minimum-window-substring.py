class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetHMap = Counter(t)
        currHMap = Counter()
        left = 0
        size = float("inf")
        minLeft = -1
        count = 0
        for right, i in enumerate(s):
            currHMap[i] += 1
            if targetHMap[i] >= currHMap[i]:
                count += 1
            while count == len(t):
                if right - left + 1 < size:
                    size = right - left + 1
                    minLeft = left

                if targetHMap[s[left]] >= currHMap[s[left]]:
                    count -= 1

                currHMap[s[left]] -= 1
                left += 1

        return "" if minLeft == -1 else s[minLeft : minLeft + size]
