class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0;
        li = []
        
        for x in amount:
            li.append(x)
        
        while(max(li) != 0):
            li.sort(reverse = True)
            a1 = li[0]
            a2 = li[1]
            a3 = li[2]
            li = []
            
            if (a2 != 0):
                ans += 1
                a1 -= 1
                a2 -= 1
                li = [a1, a2, a3]
            else:
                ans += a1
                a1 = 0
                li = [a1, a2, a3]
        
        return ans
            
        
        