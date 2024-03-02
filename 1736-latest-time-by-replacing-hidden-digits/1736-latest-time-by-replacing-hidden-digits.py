class Solution:
    def maximumTime(self, time: str) -> str:
        timeChars = list(time)

        if timeChars[0] == "?":
            timeChars[0] = "2" if (timeChars[1] < "4" or timeChars[1] == "?") else "1"

        if timeChars[1] == "?":
            timeChars[1] = "3" if timeChars[0] == "2" else "9"

        if timeChars[3] == "?":
            timeChars[3] = "5"

        if timeChars[4] == "?":
            timeChars[4] = "9"

        return "".join(timeChars)
