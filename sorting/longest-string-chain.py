class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def pred(s1, s2):
            if len(s1) + 1 != len(s2):
                return False
            f = 0
            it = 0

            for i in range(len(s2)):
                if it == len(s1):
                    return True

                if s2[i] == s1[it]:
                    it += 1
                else:
                    f += 1

                if f == 2:
                    return False

            return it == len(s1)
                


                
        dp = [1] * len(words)
        words.sort(key = lambda x: len(x))

        for i in range(len(words)):
            for j in range(i):
                if pred(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)
