class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        n = k * len(words)
        wf = Counter(words)
        sf = Counter([s[i:i+k] for i in range(0, n, k)])
        ans = []

        for i in range(0, len(s), k):
            if wf == sf:
                ans.append(i)
            
            sf[s[i+n : i+n+k]] += 1
            sf[s[i: i+k]] -= 1
            if sf[s[i: i+k]] <= 0:
                del sf[s[i: i+k]]

        return ans