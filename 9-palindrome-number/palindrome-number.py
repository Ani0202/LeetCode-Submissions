class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 0
        xcopy = x
        while x:
            y = y * 10 + x % 10
            x //= 10

        return xcopy == y
