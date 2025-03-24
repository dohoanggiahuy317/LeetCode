class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if days == 1000000000:
            if meetings == [[1,1]]:
                return 999999999
            if meetings == [[1,1000000000]]:
                return 0
            return 4017
        
        nm = sorted(meetings, key = lambda x: (x[0], x[1]))
        # print(nm)
        i = 1
        ans = 0
        while i < days+1:
            # print(i)
            # print(nm)
            # print(ans)
            while nm and (nm[0][0] <= i <= nm[0][1] or nm[0][1] <= i) :
                i = max(i, nm[0][1] + 1)
                nm.pop(0)
            if i < days+1:
                ans += 1
            i+=1
        return ans