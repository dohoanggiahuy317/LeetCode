class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])
        n = k * len(words)
        wfreq = Counter(words)
        ans = []
        
        for i in range(len(s) - n + 1):
            ns = s[i: i + n]
            
            nsfreq = Counter( [ns[j:j+k] for j in range(0, len(ns), k)] )
            if wfreq == nsfreq:
                ans.append(i)

        return ans