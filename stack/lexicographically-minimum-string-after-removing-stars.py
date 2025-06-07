import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        char = []

        for i in range(len(s)):
            if s[i] != "*":
                heapq.heappush(char, (s[i], -i))
            else:
                heapq.heappop(char)
        char.sort(key = lambda x: -x[1])
        # print(char)

        return "".join(list(map(lambda x: x[0], char)))