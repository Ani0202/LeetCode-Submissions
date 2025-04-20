class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        hmap = defaultdict(int)
        for num in answers:
            if hmap[num] == 0:
                ans += num + 1
                hmap[num] = num
            else:
                hmap[num] -= 1

        return ans
