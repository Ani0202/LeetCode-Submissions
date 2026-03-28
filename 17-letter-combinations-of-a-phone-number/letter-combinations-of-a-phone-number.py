class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def back_track(ind, tempAns):
            if ind == len(digits):
                ans.append(tempAns)
                return
            curr = digits[ind]
            for letter in hmap[curr]:
                back_track(ind + 1, tempAns + letter)

        back_track(0, "")

        return ans
