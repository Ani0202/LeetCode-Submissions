class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        while n > 1:
            i = 0
            temp = ""
            m = len(curr)
            while i < m:
                count = 1
                while i < m - 1 and curr[i] == curr[i + 1]:
                    count += 1
                    i += 1

                temp += str(count) + curr[i]
                count = 1
                i += 1

            curr = temp
            n -= 1

        return curr
