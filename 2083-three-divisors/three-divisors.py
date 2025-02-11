class Solution:
    def isThree(self, n: int) -> bool:
        divs = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if n // i == i:
                    divs += 1
                else:
                    divs += 2

        return divs == 3
