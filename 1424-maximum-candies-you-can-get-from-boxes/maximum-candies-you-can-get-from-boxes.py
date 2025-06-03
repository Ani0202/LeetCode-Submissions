from collections import deque


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)
        queue = deque(initialBoxes)
        count = 0
        while queue:
            m = len(queue)
            boxesOpened = 0
            while m:
                box = queue.popleft()
                if status[box]:
                    count += candies[box]
                    for key in keys[box]:
                        status[key] = 1

                    for innerBox in containedBoxes[box]:
                        queue.append(innerBox)

                    boxesOpened += 1
                else:
                    queue.append(box)

                m -= 1

            if boxesOpened == 0:
                break

        return count
