class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.sort()
        verticalCuts.sort()
        ansH = horizontalCuts[0]
        for i in range(1, len(horizontalCuts)):
            ansH = max(ansH, horizontalCuts[i] - horizontalCuts[i-1])
        
        ansW = verticalCuts[0]
        for i in range(1, len(verticalCuts)):
            ansW = max(ansW, verticalCuts[i] - verticalCuts[i-1])

        return (ansW * ansH) % 1000000007
        