class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        nm = sorted(meetings, key = lambda x: (x[0], x[1]))

        i = 1
        ans = 0
        while i < days+1:
            # print(i)
            while nm and nm[0][0] <= i <= nm[0][1]:
                i = nm[0][1] + 1
                nm.pop(0)
            if i < days+1:
                ans += 1
            i+=1
        return ans