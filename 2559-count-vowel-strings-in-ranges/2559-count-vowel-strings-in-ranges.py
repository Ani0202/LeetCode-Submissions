class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        arr = [0 for _ in range(n)]
        vowels = ["a", "e", "i", "o", "u"]
        if words[0][0].lower() in vowels and words[0][-1].lower() in vowels:
            arr[0] = 1
        for i in range(1, n):
            if words[i][0].lower() in vowels and words[i][-1].lower() in vowels:
                arr[i] = 1
            arr[i] += arr[i-1]

        ans = []
        for l,r in queries:
            if l != 0:
                ans.append(arr[r]-arr[l-1])
            else:
                ans.append(arr[r] - 0)
        return ans
        