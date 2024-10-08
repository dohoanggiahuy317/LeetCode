class Solution:
    def minSwaps(self, s: str) -> int:
        li = list(s)
        close_brack = 0
        ite = len(s) - 1
        ans = 0


        for i in range(len(s)):
            #print(li, close_brack)
            
            if li[i] == "[":
                close_brack -= 1
            elif li[i] == "]":
                close_brack += 1
            
                if close_brack > 0:
                    while li[ite] != "[":
                        ite -= 1
                    
                    li[i], li[ite] = li[ite], li[i]
                    ans += 1
                
                    close_brack -= 2
            
        return ans
        