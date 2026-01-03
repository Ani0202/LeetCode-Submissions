class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        i = n-1
        while i >= 0 and carry != 0:
            digits[i] += carry
            carry = digits[i] // 10
            digits[i] %= 10
            i -= 1

        if carry:
            return [carry] + digits

        return digits

        