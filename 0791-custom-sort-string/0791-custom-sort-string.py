class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap = Counter()
        let = set(order)
        ans = ""
        for i in s:
            if i in let:
                hmap[i] += 1
            else:
                ans += i

        for i in order:
            ans += i*hmap[i]
        return ans

        
        