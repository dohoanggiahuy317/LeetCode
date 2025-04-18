class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        d = []
        s = self.countAndSay(n-1)
        if len(s) == 1:
            return "1" + s
        
        curr = s[0]
        count = 1

        for i in range(1, len(s)):
            if s[i] != curr:
                d.append((count, curr))
                count = 1
                curr = s[i]
            else:
                count += 1
            
            if i == len(s) - 1:
                d.append((count, curr))
        # print(d)
        

        return "".join( list(map( lambda x: str(x[0]) + str(x[1]), d )) )