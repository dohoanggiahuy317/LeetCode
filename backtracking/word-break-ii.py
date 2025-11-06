class Solution:
    def wordBreak(self, target: str, word_dict: List[str]) -> List[str]:

        dp = defaultdict(list)
        for i in range(len(target)):
            for word in word_dict:
                if i < len(word) - 1:
                    continue

                if target[i - len(word) + 1: i + 1] == word:
                    if i == len(word) - 1:
                        dp[i].append([word])
                    else:
                        for fragmentation in dp[i - len(word)]:
                            dp[i].append(fragmentation + [word])

        sentences = dp[len(target) - 1]

        return [" ".join(part) for part in sentences]