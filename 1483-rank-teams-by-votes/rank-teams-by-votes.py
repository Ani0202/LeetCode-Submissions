class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        teams = len(votes[0])
        voteCount = defaultdict(lambda: [0 for _ in range(teams)])
        for vote in votes:
            for rank, team in enumerate(vote):
                voteCount[team][rank] += 1

        return "".join(
            sorted(
                votes[0], key=lambda team: (voteCount[team], -ord(team)), reverse=True
            )
        )
