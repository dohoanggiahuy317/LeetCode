class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        x1 = {}
        x2 = {}

        ans1 = ""
        ans2 = ""

        count = 0
        for s1 in s:
            if s1 not in x1:
                count += 1
                x1[s1] = count
            ans1 += str(x1[s1]) 

        count = 0
        for s2 in t:
            if s2 not in x2:
                count += 1
                x2[s2] = count 
            ans2 += str(x2[s2]) 

        # print(x1, x2, ans1, ans2) 

        return ans1 == ans2
        