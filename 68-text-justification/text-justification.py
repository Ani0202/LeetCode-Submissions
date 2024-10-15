class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i, n = 0, len(words)
        while i < n:
            tempAns = []
            count = len(words[i])
            tempAns.append(words[i])
            i += 1
            while i < n and count + 1 + len(words[i]) <= maxWidth:
                count += 1 + len(words[i])
                tempAns.append(words[i])
                i += 1
          
            if i == n or len(tempAns) == 1:
                leftAns = ' '.join(tempAns)
                spaceRight = ' ' * (maxWidth - len(leftAns))
                ans.append(leftAns + spaceRight)
                continue
          
            m = maxWidth - (count - len(tempAns) + 1)
            a, b = divmod(m, len(tempAns) - 1)
            c = []
            for index, word in enumerate(tempAns[:-1]):
                c.append(word)
                c.append(' ' * (a + (1 if index < b else 0)))
              
            c.append(tempAns[-1])
            ans.append(''.join(c))
          
        return ans