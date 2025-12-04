class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        r = 0
        s = False
        ans = 0
        for direction in directions:
            if direction == "L":
                if r == 0:
                    if s == True:
                        ans += 1
                else:
                    ans += r + 1
                    r = 0
                    s = True
            elif direction == "R":
                r += 1
            else:
                s = True
                ans += r
                r = 0
            print(ans)

        return ans
