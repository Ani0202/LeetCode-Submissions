class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        distinct_codes = set()
        count = 0
        total_codes = 2**k
        for i in range(n - k + 1):
            code = s[i : i + k]
            if code not in distinct_codes:
                distinct_codes.add(code)
                count += 1
            if count == total_codes:
                return True

            if n - i - k + count < total_codes:
                return False

        return True
