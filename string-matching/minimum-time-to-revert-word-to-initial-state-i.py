class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        
        
        
        
        b = False
        f = 0
        
        if len(word) % k == 0:
            for i in range(k, len(word), k):
                if word[:len(word) - i] == word[i:]:
                    b = True
                    f = i
                    break
                    
            if b == False:
                return int(len(word)/k)
            return int(i/k)
        
        
        else:
            for i in range(k, len(word), k):
                if word[:len(word) - i] == word[i:]:
                    b = True
                    f = i
                    break
                    
            if b == False:
                return int((len(word)/k)) + 1
            return int(i/k)
        return 0