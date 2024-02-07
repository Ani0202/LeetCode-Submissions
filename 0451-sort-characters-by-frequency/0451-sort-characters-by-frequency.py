class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = Counter(s)
        arr = sorted(hmap.items(), key = lambda x: -x[1])
        ans = "".join(k*v for k,v in arr)
        return ans
        