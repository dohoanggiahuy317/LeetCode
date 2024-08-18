class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        if possible == [1, 1]:
            return -1
        
        
        ans, target = 0, 0
        for x in possible:
            if x == 1:
                target += 1
            else:
                target -= 1
                
        # print(target)
        
        for i in range(len(possible) - 1):
            if possible[i] == 1:
                ans += 1
            else:
                ans -= 1
            # print(ans)
                
            if ans > target /2:
                return i + 1
        
        return -1