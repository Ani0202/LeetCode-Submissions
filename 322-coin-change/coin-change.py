from collections import deque


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited = set()

        queue = deque()
        queue.append((amount, 0))
        while queue:
            amt, count = queue.popleft()
            for val in coins:
                rem = amt - val
                if rem >= 0 and rem not in visited:
                    if rem == 0:
                        return count + 1
                    else:
                        visited.add(rem)
                        queue.append((rem, count + 1))

        return -1
