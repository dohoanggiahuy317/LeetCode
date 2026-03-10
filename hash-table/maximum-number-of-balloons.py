class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        
        return min([
                    d["b"],
                    d["a"],
                    d["l"]//2,
                    d["o"]//2,
                    d["n"]                            
                    ])