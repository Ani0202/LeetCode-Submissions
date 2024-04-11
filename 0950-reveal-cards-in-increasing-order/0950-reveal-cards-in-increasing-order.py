class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        q = deque(list(range(n)))
        ans = [0 for _ in range(n)]
        deck.sort()
        for card in deck:
            ans[q.popleft()] = card
            if len(q):
                q.append(q.popleft())
        return ans
