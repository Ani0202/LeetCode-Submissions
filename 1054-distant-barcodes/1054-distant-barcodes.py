class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hmap = defaultdict(int)
        for i in barcodes:
            hmap[i] += 1
        barcodes.sort(key=lambda x: (-hmap[x], x))
        total = len(barcodes)
        ans = [0] * total
        ans[::2] = barcodes[: (total + 1) // 2]
        ans[1::2] = barcodes[(total + 1) // 2 :]
        return ans
        