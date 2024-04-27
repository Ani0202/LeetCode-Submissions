class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for size in asteroids:
            if size > 0:
                ans.append(size)
            else:
                while ans and ans[-1] > 0 and ans[-1] < -size:
                    ans.pop()

                if ans and ans[-1] == -size:
                    ans.pop()
                elif not ans or ans[-1] < 0:
                    ans.append(size)

        return ans

        return ans
