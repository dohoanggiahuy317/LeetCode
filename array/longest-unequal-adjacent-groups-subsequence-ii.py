class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp = [1] * len(groups)
        prev = [i for i in range(len(groups))]

        for i in range(1, len(dp)):
            for j in range(i-1, -1, -1):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]):

                    if sum([ abs(ord(words[i][t]) - ord(words[j][t])) for t in range(len(words[i])) ]) == 1:
                        if dp[i] < dp[j] + 1:
                            dp[i] = dp[j] + 1
                            prev[i] = j


        curr_max = -1
        curr_ind = -1
        for i in range(len(prev)):
            if curr_max < dp[i]:
                curr_max = dp[i]
                curr_ind = i

        # print(dp)
        # print(curr_max, curr_ind)

        ans = []
        while curr_ind != prev[curr_ind]:
            ans.append(words[curr_ind])
            curr_ind = prev[curr_ind]
        ans.append(words[curr_ind])
        # print(dp)
        return ans[::-1]