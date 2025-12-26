class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            if customers[i] == "Y":
                penalty[i] = penalty[i + 1] + 1
            else:
                penalty[i] = penalty[i + 1]

        min_penalty = n + 1
        ans = -1
        curr_penalty = 0
        print(penalty)
        for i in range(n):
            if curr_penalty + penalty[i] < min_penalty:
                min_penalty = curr_penalty + penalty[i]
                ans = i
            if customers[i] == "N":
                curr_penalty += 1

        if curr_penalty + penalty[n] < min_penalty:
            min_penalty = curr_penalty + penalty[n]
            ans = n

        return ans
