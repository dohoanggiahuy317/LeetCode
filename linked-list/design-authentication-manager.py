class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.time2token = SortedDict()
        self.token2time = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.time2token[currentTime + self.ttl] = tokenId
        self.token2time[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.token2time:
            return

        old_time = self.token2time[tokenId]
        if old_time in self.time2token:
            del self.time2token[old_time]
        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        del_key = []
        for u, v in self.time2token.items():
            if u <= currentTime:
                del_key.append(u)

        for u in del_key:
            del self.time2token[u]

        return len(self.time2token)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)