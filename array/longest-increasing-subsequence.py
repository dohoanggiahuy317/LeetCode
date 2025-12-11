class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = []
        for num in nums:
            if not LIS or num > LIS[-1]:
                LIS.append(num)
            else:
                l, r = 0, len(LIS) - 1
                idx = -1
                while l <= r:
                    m = (l + r) >> 1
                    if num <= LIS[m]:
                        idx = m
                        r = m - 1
                    else:
                        l = m + 1
                LIS[idx] = num

        return len(LIS)