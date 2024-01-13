class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = "croak"
        ind = dict()
        for i,v in enumerate(croak):
            ind[v] = i
        arr = [0 for _ in range(5)]
        ans = 0
        curr = 0
        for i in croakOfFrogs:
            char = ind[i]
            if char == 0:
                curr += 1
                ans = max(ans, curr)
            else:
                if arr[char-1] <= arr[char]:
                    return -1
                if char == 4:
                    curr -= 1

            arr[char] += 1

        return -1 if curr else ans 

        