class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for size in asteroids:
            while ans and ans[-1] > 0 and size < 0 and abs(size) > abs(ans[-1]):
                ans.pop()

            if ans and ans[-1] > 0 and size < 0:
                if abs(size) == abs(ans[-1]):
                    ans.pop()
                continue

            ans.append(size)

        return ans
