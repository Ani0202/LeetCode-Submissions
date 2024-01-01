class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if digits != "":
            hmap = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
            def backTrack(digits, tempAns):
                if digits == "":
                    ans.append(tempAns)
                else:
                    for letter in hmap[digits[0]]:
                        tempAns += letter
                        backTrack(digits[1:], tempAns)
                        tempAns = tempAns[:-1]

            backTrack(digits, "")
        return ans

        