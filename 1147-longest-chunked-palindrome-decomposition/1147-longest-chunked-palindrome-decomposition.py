class Solution:
    def longestDecomposition(self, text: str) -> int:
        start = 0
        end = len(text)-1
        ans = 0
        while start <= end:
            l = 1
            found = False
            while start+l-1 < end - l+1:
                if text[start:start+l] == text[end-l+1:end+1]:
                    ans += 2
                    start += l
                    end -= l
                    found = True
                    break
                else:
                    l += 1
            if found == False:
                ans += 1
                break

        return ans
                    
        