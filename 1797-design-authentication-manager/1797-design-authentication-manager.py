class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLove = timeToLive
        self.hmap = defaultdict(int)
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.hmap[tokenId] = currentTime + self.timeToLove
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.hmap[tokenId] > currentTime:
            self.hmap[tokenId] = currentTime + self.timeToLove
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(expiry > currentTime for expiry in self.hmap.values())
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)