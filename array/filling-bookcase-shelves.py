class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        dp = [float("inf")] * (len(books)+1)
        dp[0] = 0

        for i in range(1, len(books) + 1):
            dp[i] = dp[i-1] + books[i-1][1]
            curr_width = books[i-1][0]
            for j in range(i-2, -1, -1):
                if curr_width + books[j][0] <= shelfWidth:
                    dp[i] = min( dp[j] + max(list(map(lambda x: x[1], books[j:i]))), dp[i] )
                    curr_width += books[j][0]
                else:
                    break
        return dp[-1]




