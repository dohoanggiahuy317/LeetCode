class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.time2token = SortedDict()   
        self.token2time = {}             

    def _cleanup(self, currentTime: int) -> None:
        while self.time2token and self.time2token.peekitem(0)[0] <= currentTime:
            exp_time, tokens = self.time2token.popitem(0)
            for token in tokens:
                if self.token2time.get(token) == exp_time:
                    del self.token2time[token]

    def generate(self, tokenId: str, currentTime: int) -> None:
        expire = currentTime + self.ttl
        self.token2time[tokenId] = expire
        
        if expire not in self.time2token:
            self.time2token[expire] = set()
        self.time2token[expire].add(tokenId)

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._cleanup(currentTime)

        if tokenId not in self.token2time:
            return

        old_time = self.token2time[tokenId]

        self.time2token[old_time].remove(tokenId)
        if not self.time2token[old_time]:
            del self.time2token[old_time]

        self.generate(tokenId, currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._cleanup(currentTime)
        return len(self.token2time)