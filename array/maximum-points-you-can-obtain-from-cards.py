class Solution:
    ans = 0
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        prefSum = sum(cardPoints[:k])
        ans = prefSum
        n = len(cardPoints)

        for i in range(k):
            prefSum = prefSum - cardPoints[k-1-i] + cardPoints[n-1-i]

            if prefSum > ans:
                ans = prefSum

        return ans