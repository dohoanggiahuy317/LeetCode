class Solution:
#     li = []
#     ans = []
    
#     def make_per(self, n, checking):
#         if len(self.li) == n:
#             self.ans.append("".join(self.li))
#             return
            
#         for i in range(1, n+1):
#             if checking[i-1] == True:
#                 continue
            
#             checking[i-1] = True
#             self.li.append(str(i))

#             self.make_per(n, checking)
            
#             checking[i-1] = False
#             self.li.pop(-1)
    
    def getPermutation(self, n: int, k: int) -> str:
#         checking = [False for x in range(n)]
#         self.li = []
#         self.ans = []
#         self.make_per(n, checking)
        
#         return self.ans[k-1]

        q=0
        e=[*range(1,n+1)]
        ans=""
        x=n
        while q != k and e:
            w=factorial(x-1)    
            for j in range(len(e)):
                if q+w>=k:
                    ans+=str(e.pop(j))
                    break
                q+=w
            x-=1
        return ans