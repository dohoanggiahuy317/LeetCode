class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: len(x))
        track = defaultdict(int, {"": 0})
        l, ans = 0, ""

        for word in words:
            if word[:-1] != "" and word[:-1] not in track:
                continue
            track[word] = track[ word[:-1] ] + 1
            
            if l == track[word]:
                ans = min(ans, word)
            if l < track[word]:
                ans = word
            
        return ans
            

            
            