from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        track = Counter()

        for word in words2:
            temp = Counter()
            for i in range(len(word)):
                temp[word[i]] += 1

            for u, v in temp.items():
                track[u] = max(track[u], v)


        ans = []
        for word in words1:
            temp = Counter()
            for i in range(len(word)):
                temp[word[i]] += 1

            val = True
            for u, v in track.items():
                if v > temp[u]:
                    val = False
            
            if val:
                ans.append(word)

        
        return ans

