class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hmap = Counter(arr)
        arr = sorted(hmap.keys(), key = lambda x: hmap[x])
        for i in range(len(arr)):
            k-=hmap[arr[i]]
            if k == 0:
                return len(arr)-i-1
            elif k < 0:
                return len(arr)-i