class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = defaultdict(list)

        for i in range(len(s)):

            for word in wordDict:
                if i < len(word) - 1:
                    continue

                if len(dp[i - len(word)]) > 0 or i == len(word) - 1:
                    if s[i - len(word) + 1: i + 1] == word:
                        if i == len(word) - 1:
                            dp[i].append([word])
                        else:
                            for fragmentation in dp[i - len(word)]:
                                dp[i].append(fragmentation + [word])

        sentences = dp[len(s) - 1]

        return [" ".join(part) for part in sentences]