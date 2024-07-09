class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        w = 0
        s = customers[0][0]

        for e, t in customers:
            if e >= s:
                s = e + t
                w += t
            else:
                s = s+t
                w += (s - e)
            # print(s, w)

        return w/len(customers)
            