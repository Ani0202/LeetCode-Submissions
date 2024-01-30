class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        col = defaultdict(list)
        for x, y in points:
            col[x].append(y)
    
        lastx = {}
        ans = float('inf')
    
        for x in sorted(col):
            column = col[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
    
        if ans < float('inf'):
            return ans
        else:
            return 0
        