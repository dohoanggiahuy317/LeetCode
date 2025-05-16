class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [1] * len(groups)

        for i in range(1, len(dp)):
            for j in range(i-1, -1, -1):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):
                    if sum([ abs(ord(words[i][t]) - ord(words[j][t])) for t in range(len(words[i])) ]) == 1:
                        dp[i] = max(dp[j] + 1, dp[i])


        # print(dp)
        return max(dp)