class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        distinct_codes = set()
        for i in range(len(s) - k + 1):
            distinct_codes.add(s[i : i + k])

        return len(distinct_codes) == 2**k
