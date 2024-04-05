class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a,b):
            while b:
                a,b = b,a%b
            return a

        ans = []
        for num in nums:
            while len(ans) and gcd(ans[-1], num) > 1:
                lNum = ans.pop()
                num = lNum*num/gcd(lNum, num)
            ans.append(int(num))
        return ans
        