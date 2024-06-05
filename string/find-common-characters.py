class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []

        bd = []

        for word in words:
            d = Counter()
            for char in word:
                d[char] += 1
            bd.append(d)

        for u in words[0]:
            ans.append(u)
            for d in bd:
                if d[u] <= 0:
                    ans.pop(-1)
                    break
                print(d)
                d[u] -= 1
            print()
            
        return ans