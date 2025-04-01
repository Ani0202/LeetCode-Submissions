class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        points = [0 for _ in range(n)]
        points[n - 1] = questions[n - 1][0]
        maxPoints = questions[n - 1][0]
        for i in range(n - 2, -1, -1):
            point, brainpower = questions[i]
            points[i] = max(
                point
                + (0 if i + brainpower + 1 > n - 1 else points[i + brainpower + 1]),
                points[i + 1],
            )
            maxPoints = max(maxPoints, points[i])

        return maxPoints
