class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        d = {}

        for x in chars:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1

        for word in words:
            newd = {}
            b = True
            for x, y in d.items():
                newd[x] = y
            
            for char in word:
                if char in newd:
                    newd[char] -= 1
                else:
                    b = False
                    break

                if newd[char] < 0:
                    b = False
                    break

            # print(word, newd)
            if b:
                ans += len(word)

        return ans