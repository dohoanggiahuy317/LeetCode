class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        def find_LIS(li):
            LIS = []
            LIS.append(li[0])

            for i in range(1, len(li)):
                num = li[i]

                if LIS[-1] < num:
                    LIS.append(num)
                elif LIS[-1] > num:
                    l, r = 0, len(LIS) - 1
                    idx = -1
                    while l <= r:
                        m = (l + r) // 2
                        if LIS[m] >= num:
                            idx = m
                            r = m - 1
                        else:
                            l = m + 1
                    LIS[idx] = num
            
            return len(LIS)


        envelopes.sort(key = lambda x: (x[0], -x[1]))
        return find_LIS([envelope[1] for envelope in envelopes])
