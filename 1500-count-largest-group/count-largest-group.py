class Solution:
    def countLargestGroup(self, n: int) -> int:
        hmap = defaultdict(list)

        def findSum(num):
            s = 0
            while num:
                s += num % 10
                num //= 10

            return s

        for i in range(1, n + 1):
            count = findSum(i)
            hmap[count].append(i)

        maxLen = max(len(val) for val in hmap.values())
        ans = 0
        for val in hmap.values():
            if len(val) == maxLen:
                ans += 1

        return ans
