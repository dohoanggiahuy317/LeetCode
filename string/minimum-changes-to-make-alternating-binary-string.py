class Solution:
    def minOperations(self, s: str) -> int:
        l = len(s)

        t1 = ""
        t2 = ""

        for i in range(l):
            t1 += "10"
            t2 += "01"

        if l % 2 != 0:
            t1 = t1[1:]
            t2 = t2[1:]

        # print(t1, t2)

        count1 = 0
        count2 = 0

        for i in range(l):
            if s[i] != t1[i]:
                count1 += 1
            if s[i] != t2[i]:
                count2  += 1
            
        return min(count1, count2)
