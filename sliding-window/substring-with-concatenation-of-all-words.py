class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, m = len(words) * len(words[0]), len(words[0])
        cw = Counter(words)
        ans = []

        for i in range(len(s) - n + 1):
            chunk = s[i: i + n]
            l = len(chunk)
            # print(list(chunk[j:j + m] for j in range(0, l, m)))
            if cw == Counter( list(chunk[j:j + m] for j in range(0, l, m)) ):
                ans.append(i)
        
        return ans