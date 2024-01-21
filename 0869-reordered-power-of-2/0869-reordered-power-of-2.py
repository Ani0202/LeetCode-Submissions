class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def countDigits(num):
            count = [0] * 10
            while num:
                num, digit = divmod(num, 10)
                count[digit] += 1
            return count
        numCount = countDigits(n)
        two = 1
        while two <= 10**9:
            if countDigits(two) == numCount:
                return True
            two <<= 1
        return False