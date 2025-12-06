class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        def find_LIS(arr):
            LIS = []
            LIS.append(arr[0])

            for i in range(1, len(arr)):
                num = arr[i]

                if LIS[-1] < num:
                    LIS.append(num)
                else:
                    l, r = 0, len(LIS) - 1
                    idx = -1

                    while l <= r:
                        m = (l + r) // 2
                        if num <= LIS[m]:
                            idx = m
                            r = m - 1
                        else:
                            l = m + 1
                    
                    LIS[idx] = num

            return len(LIS)

        envelopes.sort(key = lambda x: (x[0], -x[1]))

        return find_LIS([envelope[1] for envelope in envelopes])

