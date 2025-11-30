class ATM:

    def __init__(self):
        self.den = [20, 50, 100, 200, 500]
        self.count = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, val in enumerate(banknotesCount):
            self.count[i] += val

    def withdraw(self, amount: int) -> List[int]:
        ans = []
        count_arr = [0] * 5
        for i in range(len(self.den) - 1, -1, -1):
            count = min(self.count[i], amount // self.den[i])
            count_arr[i] = count
            amount -= self.den[i] * count
            ans.append(count)

        if amount == 0:
            for i in range(4, -1, -1):
                self.count[i] -= count_arr[i]
            return ans[::-1]

        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
