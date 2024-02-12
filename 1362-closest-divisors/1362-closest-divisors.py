class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def findClosestDivisors(n):
            for i in range(int(n**0.5), -1, -1):
                if n % i == 0:
                    return [i, n // i]

        d1, d2 = findClosestDivisors(num + 1)
        d3, d4 = findClosestDivisors(num + 2)
        return [d1, d2] if abs(d1 - d2) <= abs(d3 - d4) else [d3, d4]
