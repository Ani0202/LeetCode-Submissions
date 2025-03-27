class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return "Flush"
        
        rankMap = defaultdict(int)
        for rank in ranks:
            rankMap[rank] += 1

        pair = False
        for val in rankMap.values():
            if val >= 3:
                return "Three of a Kind"
            if val >= 2:
                pair = True

        if pair:
            return "Pair"

        return "High Card"