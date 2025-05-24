class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        p11 = 0
        p12 = 0
        p21 = 0
        p22 = 0
        p1 = 0
        p2 = 0
        for i in range(n):
            p1 += player1[i]
            p2 += player2[i]
            if p11 == 10 or p12 == 10:
                p1 += player1[i]

            if p21 == 10 or p22 == 10:
                p2 += player2[i]

            p11, p12 = p12, player1[i]
            p21, p22 = p22, player2[i]

        if p1 > p2:
            return 1
        elif p2 > p1:
            return 2
        else:
            return 0
