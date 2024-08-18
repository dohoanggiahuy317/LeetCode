class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter()

        for x in list(text):
            d[x] += 1

        # print(d)

        return min([
                    d["b"],
                    d["a"],
                    d["l"]//2,
                    d["o"]//2,
                    d["n"]                            
                    ])