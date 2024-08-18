class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        # n = len(nums)
        # diffs = [nums[i] - target[i] for i in range(n)]
        
        # ans = 0
        # i = 0
        
        # while i < n:
        #     if diffs[i] != 0:
        #         sign = 1 if diffs[i] > 0 else -1
        #         j = i
        #         while j < n and diffs[j] * sign > 0:
        #             diffs[j] -= sign
        #             j += 1
        #         ans += 1
        #     else:
        #         i += 1
        
        # return ans

        n = len(nums)
        diffs = [nums[i] - target[i] for i in range(n)]
        
        ans = 0
        i = 0
        
        while i < n:
            if diffs[i] != 0:
                sign = 1 if diffs[i] > 0 else -1
                j = i
                m_v = float('inf')
                
                while j < n and diffs[j] * sign > 0:
                    m_v = min(m_v, abs(diffs[j]))
                    j += 1
                
                for k in range(i, j):
                    diffs[k] -= sign * m_v
                
                ans += m_v
            else:
                i += 1
        
        return ans