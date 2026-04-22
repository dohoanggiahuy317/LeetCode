class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        curr = sum(cardPoints[:k])
        ans = curr
        
        for i in range(k):
            curr = curr - cardPoints[k-1-i] + cardPoints[n-1-i]
            ans = max(ans, curr)

        return ans