class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLove = timeToLive
        self.hmap = dict()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hmap[tokenId] = currentTime + self.timeToLove
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hmap and self.hmap[tokenId] > currentTime:
            self.hmap[tokenId] = currentTime + self.timeToLove
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        ans = 0
        for v in self.hmap.values():
            ans += 1 if v > currentTime else 0
        return ans
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)